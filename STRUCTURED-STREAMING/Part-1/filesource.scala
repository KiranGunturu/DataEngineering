# will be getting new files in my input folder
# task is to filter the completed orders and put it in a output file

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
						.config("spark.sql.streaming.schemaInference","true") \
                        .getOrCreate()
    
    #1.read from file source
    
    val ordersDf = spark\
            .readStream \
            .format("json") \
            .option("path", "/input/file/path") \
			.option("maxFilesPerTrigger",1) \
            .load()
            
    linesDf.printSchema()
            
    #2. process
    
    ordersDf.createOrReplaceTempView("orders")
	
	val completedOrders = spark.sql("select *from orders where order_status="COMPLETE")
    
    
    
    #3. write to the file
    
    val ordersQuery = completedOrders.writeStream \
                            .format("json") \
                            .outputMode("append") \
                            .option("checkpointlocation","/usr/customer/") \
							.option("path","myoutputfolder"
                            .trigger(Trigger.ProcessingTime("30 seconds")) \
                            .start() # acts like an action
    
    ordersQuery.awaitTermination()
    
    
    