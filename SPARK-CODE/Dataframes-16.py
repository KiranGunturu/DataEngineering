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

    # String expression way

    ordersDF_csv.selectExpr("count(*) as RowCount",
                            "sum(Quantity) as TotalQuantity",
                            "avg(UnitPrice) as AvgPrice",
                            "count(Distinct(InvoiceNo)) as CountDistinct"
                            ).show()
    # spark sql way
    # sales is table and distributed across the cluster

    ordersDF_csv.createOrReplaceTempView("sales")

    spark.sql("""select count(*) as totalCount, sum(Quantity) as TotalQuantity, avg(UnitPrice) as avgPrice,
    count(distinct(InvoiceNo)) as distinctive 
    from sales""").show()
