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


if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Reading styles") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    window_csv = spark.read \
        .format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK/windowdata.csv") \
        .load()


    # window_csv.show()

    my_window = Window.partitionBy("Country").orderBy("weeknum").rowsBetween(Window.unboundedPreceding, Window.currentRow)

    window_df = window_csv.withColumn("running_total",sum("invoicevalue").over(my_window))

    window_df.show()


