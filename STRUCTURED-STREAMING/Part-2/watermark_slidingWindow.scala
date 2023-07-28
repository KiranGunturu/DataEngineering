
# calculate amount of sales every 15 mins with 30 mins watermark window
# sliding interval

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
	
	val orderSchema = StructType(
		[
		StructField("order_id", IntegerType())
		StructField("order_date", TimestampType())
		StructField("order_customer_id", IntegerType())
		StructField("order_status", StringType())
		StructField("amount", IntegerType()),
		)
		]
    
    #1.read from socket
    
    val ordersDf = spark\
            .readStream \
            .format("socket") \
            .option("host", "localhost") \
			.option("port",12345) \
            .load()
			
	#ordersDf.printSchema()
	
	# process
	
	val valueDf = ordersDf.select(from_json(col("value"), orderSchema).alias("value")
	
	#valueDf.printSchema()
	
	val refinedOrdersDf = valueDf.select("value.*")
	
	#refinedOrdersDf.printSchema()
	
	val windowAggDf = refinedOrdersDf \
									.withWatermark("order_date", "30 minute") \
									.groupBy(window(col("order_date"), "15 minute", "5 minute")) \
									.agg(sum("amount")) \
									.alias("totalInvoice")
	
	
    #windowAggDf.printSchema()

	val outputDf = windowAggDf.select("window.start","window.end","totalInvoice")	
	
	# write to the sink
	
	val ordersQuery = outputDf.writeStream \
							.format("console") \
							.outputMode("update") \
							.option("checkpointLocation","/path") \
							.trigger(Trigger.ProcessingTime("15 second")) \
							.start()
    
	
	ordersQuery.awaitTermination()