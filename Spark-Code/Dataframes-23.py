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
    # data = [
    #     ["WARN, 2016-12-31 04:19:32"],
    #     ["FATAL, 2016-12-31 03:22:34"],
    #     ["WARN, 2015-4-21 14:32:21"],
    #     ["FATAL, 2015-4-21 19:23:20"]
    # ]
    #
    # rdd1 = spark.sparkContext.parallelize(data)

    big_log = spark.read \
        .option("header", "true") \
        .csv("/Users/kirangunturu/Documents/WEEK12-SPARK/biglog.txt")

    big_log.createOrReplaceTempView("new_log_table")

    results = spark.sql("""select level, date_format(datetime,'MMM') as month, count(*) as total from new_log_table 
    group by level, month""")

    results.createOrReplaceTempView("results_table")

    # results1 = spark.sql("""select level, date_format(datetime,'MMM') as month, cast(first(date_format(datetime,'M')) as int) as monthnum, count(*) as total
    #     from new_log_table
    #     group by level, month order by monthnum, level""")

    # results2 = results1.drop("monthnum").show()

    results1 = spark.sql("""select level, date_format(datetime,'MMM') as month, 
            cast(date_format(datetime,'M') as int) as monthnum
            from new_log_table""").groupby("level").pivot("monthnum").count().show(100)











