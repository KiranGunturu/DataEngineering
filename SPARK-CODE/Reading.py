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

    # ordersDF_csv = spark.read \
    #     .format("csv") \
    #     .option("header", "true") \
    #     .option("inferSchema", "true") \
    #     .option("path", "/Users/kirangunturu/Documents/WEEK11-SPARK/orders.csv") \
    #     .load()
    #
    # ordersDF_csv.show(5, False)
    # ordersDF_csv.printSchema()

    # Read JSON

    # json does not have any header
    # json by default infers schema

    # ordersDF_json = spark.read \
    #     .format("json") \
    #     .option("path", "/Users/kirangunturu/Documents/WEEK11-SPARK/players.json") \
    #     .load()
    #
    # ordersDF_json.printSchema()
    #
    # ordersDF_json.show(5, False)

    # Malformed

    # PERMISSIVE - DEFAULT ONE

    # ordersDF_json_mf_permissive = spark.read \
    #     .format("json") \
    #     .option("path", "/Users/kirangunturu/Documents/WEEK11-SPARK/players_error.json") \
    #     .load()
    #
    # ordersDF_json_mf_permissive.printSchema()
    #
    # ordersDF_json_mf_permissive.show(truncate=False)

    # DROP MALFORMED MODE - IT WILL DROP CORRUPTED RECORDS

    # ordersDF_json_dropmf = spark.read \
    #     .format("json") \
    #     .option("path", "/Users/kirangunturu/Documents/WEEK11-SPARK/players_error.json") \
    #     .option("mode","DROPMALFORMED") \
    #     .load()
    #
    # ordersDF_json_dropmf.printSchema()
    #
    # ordersDF_json_dropmf.show(truncate=False)

    # FAILFAST MODE - THROW AN EXCEPTION

    # ordersDF_json_ffast = spark.read \
    #     .format("json") \
    #     .option("path", "/Users/kirangunturu/Documents/WEEK11-SPARK/players_error.json") \
    #     .option("mode", "FAILFAST") \
    #     .load()
    #
    # ordersDF_json_ffast.printSchema()
    #
    # ordersDF_json_ffast.show(truncate=False)

    # READ PARQUET FILE
    # in spark by default .format is the parquet so that's why did not mentioned anything below

    ordersDF_parquet = spark.read \
        .option("path", "/Users/kirangunturu/Documents/WEEK11-SPARK/users.parquet") \
        .load()

    ordersDF_parquet.printSchema()

    ordersDF_parquet.show(truncate=False)
