from pyspark import SparkContext
from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import column, col, expr, unix_timestamp, monotonically_increasing_id, row_number
from pyspark.sql.types import StructType, StructField, IntegerType, DateType, StringType

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Reading styles") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # dummy data
    data = [
        [1, '2013-07-25', 11599, "CLOSED"],
        [2, '2014-07-25', 256, "PENDING_PAYMENT"],
        [3, '2013-07-25', 11599, "COMPLETE"],
        [4, '2019-07-25', 8827, "CLOSED"]
    ]

    # attach schema as string
    # columns = ["id", "order_date", "order_id", "order_status"]

    # struct schema programmatically
    schema = StructType(
        [
            StructField("id", IntegerType()),
            StructField("order_date", StringType()),
            StructField("customer_id", IntegerType()),
            StructField("order_status", StringType())
        ])

    # create dataframe
    orders_df = spark.createDataFrame(data=data, schema=schema)

    # convert order_date column to epoch time

    order_df_epoch = orders_df.withColumn("order_date", unix_timestamp(col("order_date").cast(DateType())))

    # add unique row number to the dataframe

    orders_new_id = order_df_epoch.withColumn("unique_id", monotonically_increasing_id()) \
        .withColumn("increasing_id", row_number().over(Window.orderBy("unique_id"))) \
        .drop("unique_id")

    # drop duplicates based on order_date and customer_id

    drop_df = orders_new_id.dropDuplicates(["order_date", "customer_id"]) \
        .drop("id") \
        .sort("order_date")

    drop_df.show()
