from sys import stdin
from pyspark import SparkContext
from pyspark.sql import SparkSession

if __name__ == "__main__":
    # create spark session
    spark = SparkSession \
        .builder \
        .appName("Dataframes-3 coding") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("INFO")

    # reading file
    orders_df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv("/Users/kirangunturu/Documents/WEEK11-SPARK/orders.csv")

    transformed_df = orders_df\
        .repartition(4) \
        .where("order_customer_id > 10000") \
        .select("order_id", "order_customer_id") \
        .groupBy("order_customer_id") \
        .count()

    transformed_df.foreach(lambda x: print(x))

    transformed_df.show()

    stdin.readline()

    spark.stop()
