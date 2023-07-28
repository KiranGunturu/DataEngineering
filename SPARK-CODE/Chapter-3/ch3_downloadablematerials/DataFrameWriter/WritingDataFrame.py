from pyspark.sql import *
from pyspark.sql.functions import to_date, when, col

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("WritingDataFrame") \
        .getOrCreate()

    flight_schema_ddl = """FL_DATE STRING, OP_CARRIER STRING, OP_CARRIER_FL_NUM INT, ORIGIN STRING, 
             ORIGIN_CITY_NAME STRING, DEST STRING, DEST_CITY_NAME STRING, CRS_DEP_TIME INT, DEP_TIME INT, 
             WHEELS_ON INT, TAXI_IN INT, CRS_ARR_TIME INT, ARR_TIME INT, CANCELLED STRING, DISTANCE INT"""

    flight_time_raw_df = spark.read \
        .format("json") \
        .schema(flight_schema_ddl) \
        .option("mode", "FAILFAST") \
        .option("dateFormat", "M/d/y") \
        .load("data/flight-time.json")

    flight_time_df = flight_time_raw_df \
        .withColumn("FL_DATE", to_date("FL_DATE", "M/d/y")) \
        .withColumn("CANCELLED", when(col("CANCELLED") == "1", True).otherwise(False))

    flight_time_df.show(10)

    input("Press Enter to Finish...")
