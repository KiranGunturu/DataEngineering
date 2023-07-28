from pyspark import SparkContext
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Reading styles") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # cmd / to comment and uncomment
    # Read CSV

    ordersDF_csv = spark.read \
        .format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .option("path", "/Users/kirangunturu/Documents/WEEK11-SPARK/orders.csv") \
        .load()

    ordersDF_csv.createOrReplaceTempView("orders")

    #resultDF = spark.sql("select order_status,count(*) as cnt from orders group by order_status order by cnt desc")

    customerDF = spark.sql("select order_customer_id,count(*) as cnt from orders where order_status = 'CLOSED' \
    group by order_customer_id order by cnt desc")

    customerDF.show()



