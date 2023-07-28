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

    # if we do not mention any format when we write then by default it is parquet
    # csv format
    # ordersDF_csv.write \
    #     .format("csv") \
    #     .mode("overwrite") \
    #     .option("path","/Users/kirangunturu/Documents/WEEK12-SPARK") \
    #     .save()

    # json
    # ordersDF_csv.write \
    #     .format("json") \
    #     .mode("overwrite") \
    #     .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK") \
    #     .save()

    # parquet

    # ordersDF_csv.write \
    #     .mode("overwrite") \
    #     .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK") \
    #     .save()

    # ordersDF_csv.write \
    #     .mode("append") \
    #     .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK") \
    #     .save()

    print("orderDF_csv has " + str(ordersDF_csv.rdd.getNumPartitions()))

    ordersDF_rep = ordersDF_csv.repartition(4)

    print("ordersDF_rep has "+ str(ordersDF_rep.rdd.getNumPartitions()))

    # ordersDF_rep.write \
    #     .format("csv") \
    #     .mode("overwrite") \
    #     .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK") \
    #     .save()

    # partitionBy
    # below code will create 4 csv files for each partition as we repartitioned to 4 above

    # ordersDF_rep.write \
    #     .format("csv") \
    #     .mode("overwrite") \
    #     .partitionBy("order_status") \
    #     .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK") \
    #     .save()

    # control the number of lines in each file

    # ordersDF_rep.write \
    #     .format("csv") \
    #     .mode("overwrite") \
    #     .option("maxRecordsPerFile",2000) \
    #     .partitionBy("order_status") \
    #     .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK") \
    #     .save()

    # save as avro?
    # by default spark will not support avro, but it will if we add a jar file
    # same like xml

    ordersDF_rep.write \
        .format("avro") \
        .mode("overwrite") \
        .option("maxRecordsPerFile", 2000) \
        .partitionBy("order_status") \
        .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK") \
        .save()
