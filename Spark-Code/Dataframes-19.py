from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import column, col, expr, unix_timestamp, monotonically_increasing_id, row_number, broadcast
from pyspark.sql.types import StructType, StructField, IntegerType, DateType, StringType
from sys import stdin

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Reading styles") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")
    # orders
    orders = spark.read \
         .format("csv") \
         .option("header", "true") \
        .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK/orders.csv") \
        .load()
    # orders.show()
    # customers
    customers = spark.read \
        .format("csv") \
        .option("header", "true") \
        .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK/customers.csv") \
        .load()
    # customers.show()
    join_condition = orders.order_customer_id == customers.customer_id
    join_type = "outer"

    # spark.sql("SET spark.sql.autoBroadcastJoinThreshold = -1")
    # spark.conf.set("spark.sql.adaptive.enabled", False)

    join_df = orders.join(broadcast(customers),join_condition,join_type).sort("order_customer_id")

    join_df.show()

    stdin.readline()


