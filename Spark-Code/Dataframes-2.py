from pyspark.sql import SparkSession
from sys import stdin

spark = SparkSession \
        .builder \
        .appName("loading the file") \
        .master("local[*]") \
        .getOrCreate()

ordersdf = spark.read \
                .option("header","true") \
                .option("inferSchema","true") \
                .csv("/Users/kirangunturu/Documents/WEEK11-SPARK/orders.csv")


#ordersdf.show(10,False)

print(ordersdf.printSchema())

stdin.readline()