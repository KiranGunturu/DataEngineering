

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
	
	val transactioSchema = StructType([
							StructField("card_id",LongType),
							StructField("amout",IntegerType),
							StructField("postal_code",IntegerType),
							StructField("pos_id",LongType),
							StructField("transaction_dt",TimestampType)
							])
							
	val txnDf = 	spark.readStream \
						.format("socket") \
						.option("host","localhost") \
						.option("port", 12343) \
						.load()
	#txnDf.printSchema() 
	
	root
		|--value: string(nullable = true)
	
	val valueDf = txnDf.select(from_json(col("value"),transactioSchema).alias("value")
	
	#valueDf.printSchema()
	
	root
		|--value: struct(nullable = true)
			|-- card_id: long (nullable = true)
			|-- amount: integer (nullable = true)
	
	val refinedTxnDf valueDf.select("value.*") //bring all cols at root level
	
	#refinedTxnDf.printSchema()
	
	root
		|-- card_id: long (nullable = true)
		|-- amount: integer (nullable = true)
		
	//load the static Df
	
	val memberDf = spark \
					.read \
					.format("csv") \
					.option("header","true") \
					.option("inferSchema" ,"true") \
					.option("path", "/users/member_details") \
					.load()
					
	
	
	val joinExpr = refinedTxnDf.col("card_id") === memberDf.col("card_id")
	
	val joinType = "left"
	
	
	val enrichedDf = refinedTxnDf.join(memberDf,joinExpr,joinType).drop(memberDf.col("card_id"))
	
	//write to the sink
	
	val txnQuery = enrichedDf.writeStream \
						.format("console") \
						.outputMode("update") \
						.option("checkpointLocation", "/user/path/") \
						.trigger(Trigger.ProcesingTime("15 second")) \
						.start()
	
	txnQuery.awaitTermination()