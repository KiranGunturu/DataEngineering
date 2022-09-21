import sys
from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("My Application 1") \
        .master("local[*]") \
        .getOrCreate()

print(spark.version)

spark.stop()



