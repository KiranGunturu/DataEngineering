from pyspark import SparkContext
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Reading styles") \
        .master("local[*]") \
        .enableHiveSupport() \
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

    # sometimes we have a req to save the data in a persistent manner in the form of table
    # when the data is stored in the form of table then we can connect tableau, power bi etc. for reporting purpose.

    # table as 2 parts

    # data and metadata
    # spark-warehouse for data catalog metastore for metadata

    # spark.sql.warehouse.dir in memory (on terminating application it is gone)
    # we can use hive metastore to handle spark metadata.

    # # create a database
    #
    # spark.sql("create database if not exists retail")
    #
    # ordersDF_csv.write \
    #     .format("csv") \
    #     .mode("overwrite") \
    #     .saveAsTable("retail.orders1")

    # this table will be created in spark-warehouse and metadata will be gone after application is stopped.
    # so to avoid this we add a hive jar in scala
    # for pyspark just add enableHiveSupport to the spark session

    # create a database

    spark.sql("create database if not exists retail")

    ordersDF_csv.write \
        .format("csv") \
        .mode("overwrite") \
        .bucketBy(4,"order_customer_id") \
        .sortBy("order_customer_id") \
        .saveAsTable("retail.orders3")

    print(spark.catalog.listTables("retail"))

    # this will now create hive metastore and also the retail db and table in spark-warehouse
    # now the metadata will be stored in hive metastore instead spark metastore which will go away once app is finished
    # and bucket By only works when we say saveAsTable








