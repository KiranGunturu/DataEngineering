import org.apache.spark.SparkContext
import org.apache.spark.streaming.Seconds
import org.apache.spark.log4j.Level
import org.apache.spark.Logger
import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object StreamingWordCount extends App {
    Logger.getLogger("org").setLevel(Level.ERROR)
    
    val spark = SparkSession.builder()\
                        .master("local[2]") \
                        .appName("My Streaming Application") \
                        .config("spark.sql.shuffle.partitions",3) \ #by default we get 200 partitions
                        .config("spark.streaming.stopGracefullyOnShutdown","true") \
                        .getOrCreate()
    
    #1.read from the stream
    
    val linesDf = spark\
            .readStream \
            .format("socket") \
            .option("host", "localhost") \
            .option("port","12345") \
            .load()
            
    linesDf.printSchema()
            
    #2. process
    
    val wordsDf = linesDf.selectExpr("explode(split(value,' ')) as word")
    val countDF = wordsDf.groupBy("word").count()
    
    #i/p hello hello how are you
    # split(value,' ') - gives an array [hello, hello, how, are, you]
    #explode(split(value,' ')) it will break the array
        #hello
        #hello
        #how
        #are
        #you
    
    #3. write to the sink
    
    val wordCountQuery = linesDf.writeStream \
                            .format("cosole") \
                            .outputMode("complete") \
                            .option("checkpointlocation","/usr/customer/") \
                            .trigger(Trigger.ProcessingTime("30 seconds")) \
                            .start() # acts like an action
    
    wordCountQuery.awaitTermination()
    
    #thats why when we do aggeregations append mode is not allowed
    # append outputMode is supported when we do streaming aggregations
    