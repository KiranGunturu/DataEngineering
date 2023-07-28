

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
						
	//defining the schema for Impressions stream
	
	val impressionSchema = StructType([
							StructField("impressionID",StringType),
							StructField("impressionTime",TimestampType),
							StructField("campaignName",StringType)
							])
							
	//defining the schema for Clicks stream
	
	val clickSchema = StructType([
							StructField("clickID",StringType),
							StructField("clickTime",TimestampType)
							])
	
	//read data from socket - Impressions
	
	val impressionsDf = spark.readStream \
							.format("socket") \
							.option("host","localhost") \
							.option("port", 12343) \
							.load()
								
	//read data from socket - Clicks
	
	val clicksDf = spark.readStream \
						.format("socket") \
						.option("host","localhost") \
						.option("port", 12344) \
						.load()
	
	
	
	//structure the data based on the schema defined - ImpressionsDf
	
	val valueDf1 = impressionsDf.select(from_json(col("value"),impressionSchema).alias("value")
	val impressionsDfNew = valueDf1.select("value.*").withWatermark("impressionTime","30 minute") //bring all cols at root level
	
	//structure the data based on the schema defined - ClicksDf
	
	val valueDf2 = clicksDf.select(from_json(col("value"),clickSchema).alias("value")
	val clicksDfNew = valueDf2.select("value.*").withWatermark("clickTime","30 minute") //bring all cols at root level
		
	
	//join condition
	val joinExpr = impressionsDfNew.col("impressionID") === clicksDfNew.col("clickID")
	
	//join type
	val joinType = "inner"
	
	//join both the streaming dataframes
	val joinedDf = impressionsDfNew.join(clicksDfNew,joinExpr,joinType).drop(clicksDfNew.col("clickID"))
	
	//write to the sink
	
	val campaignQuery = joinedDf.writeStream \
							.format("console") \
							.outputMode("append") \
							.option("checkpointLocation", "/user/path/") \
							.trigger(Trigger.ProcesingTime("15 second")) \
							.start()
	
	campaignQuery.awaitTermination()