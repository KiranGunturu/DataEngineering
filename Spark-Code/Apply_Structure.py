from pyspark.sql.types import StructType, StructField, IntegerType, TimestampType, StringType
from pyspark import SparkContext
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Reading styles") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # Programmatic way of giving schema

    orders_schema = StructType([
                StructField("orderid",IntegerType(),False),
                StructField("orderdate",TimestampType()),
                StructField("customerid", IntegerType()),
                StructField("status", StringType())
    ])

    # Read CSV

    ordersDF_csv = spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(orders_schema) \
        .option("path", "/Users/kirangunturu/Documents/WEEK11-SPARK/orders.csv") \
        .load()

    # ordersDF_csv.show(5, False)
    # ordersDF_csv.printSchema()

    # DDL String - we should not be giving spark datatypes with this approach but python types

    orders_schema_ddl_string = "Orderid Int, order_date Timestamp, customer_id Int, order_status String"

    # Read CSV

    ordersDF_csv_ddl_string = spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(orders_schema_ddl_string) \
        .option("path", "/Users/kirangunturu/Documents/WEEK11-SPARK/orders.csv") \
        .load()

    ordersDF_csv_ddl_string.show(5, False)
    ordersDF_csv_ddl_string.printSchema()