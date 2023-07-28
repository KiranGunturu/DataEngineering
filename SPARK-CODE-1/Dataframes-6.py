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

    import spark.implicits._

    spark.sparkContext.setLogLevel("INFO")

    # reading file
    orders_df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv("/Users/kirangunturu/Documents/WEEK11-SPARK/orders.csv")

    # orders_df.filter("order_ids < 10")
    # though column order_ids does not exist it is not giving us any error here but we get at run time

    orders_df.filter("order_id < 10")
