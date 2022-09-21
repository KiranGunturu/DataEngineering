from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import column, col, expr

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Reading styles") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # cmd / to comment and uncomment
    # Read CSV

    ordersDF_csv = spark.read \
        .format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK/orders.csv") \
        .load()

    # column string
    # ordersDF_csv.select("order_id","order_Status").show()

    # column object using either column or col

    # ordersDF_csv.select(column("order_id"),col("order_status")).show()

    # column expressions

    # ordersDF_csv.select("order_id","order_date",expr("concat(order_status,'_STATUS')")).show(truncate=False)

    # to make above one simple use selectExpr - This will allow us to give everything as a string

    ordersDF_csv.selectExpr("order_id", "order_date", "concat(order_status,'_STATUS')").show(truncate=False)









