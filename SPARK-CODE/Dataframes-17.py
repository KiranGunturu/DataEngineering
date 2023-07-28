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

    ordersDF_csv = spark.read \
        .format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK/order_data.csv") \
        .load()
# string expression
    summary_df = ordersDF_csv.groupby("Country","InvoiceNo") \
        .agg(expr("sum(Quantity) as totalQuantity"),
             expr("sum(Quantity * UnitPrice) as InvoiceValue"))

# spark sql way

    ordersDF_csv.createOrReplaceTempView("Sales")

    spark.sql("""select Country, InvoiceNo,
    sum(Quantity) as totalQuantity, sum(Quantity * UnitPrice) as InvoiceValue 
    from sales 
    group by Country,InvoiceNo""")\
        .show()

