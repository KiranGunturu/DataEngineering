from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Reading styles") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # cmd / to comment and uncomment
    # Read CSV
    my_regex = r'^(\S+) (\S+)\t(\S+)\,(\S+)'

    lines = spark.read.text("/Users/kirangunturu/Documents/WEEK12-SPARK/orders_new.csv")

    # lines.printSchema()

    # lines.show()

    finaldf = lines.select(regexp_extract('value',my_regex,1).alias("order_id"),
                           regexp_extract('value',my_regex,2).alias("date"),
                           regexp_extract('value',my_regex,3).alias("customer_id"),
                           regexp_extract('value',my_regex,4).alias("status"))

    finaldf.printSchema()

    # finaldf.show()

    finaldf.groupby("status").count().show()


