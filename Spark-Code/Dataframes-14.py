from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import column, col, expr, md5, concat_ws, udf
from pyspark.sql.types import StringType

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Reading styles") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    def age_check(age):
        if age > 18:
            return 'Y'
        else:
            return 'N'

    # cmd / to comment and uncomment
    # Read CSV

    dataset = spark.read \
        .format("csv") \
        .option("inferSchema", "true") \
        .option("path", "/Users/kirangunturu/Documents/WEEK12-SPARK/dataset1") \
        .load()

    # hashed = dataset.withColumn("Hash",md5(concat_ws("",*dataset.columns)))

    # hashed.show()

    dataset1 = dataset.toDF("NAME","AGE","CITY")

    # dataset1.printSchema()

    # dataset1.show(5,False)

    # COLUMN object notation and this wont be registered in the catalog

    # parse_age_function = udf(age_check, StringType())
    #
    # df2 = dataset1.withColumn("adult",parse_age_function("AGE"))
    #
    # df2.show()

    # SQL Expression of udf which will register the

    spark.udf.register("parse_age_function",age_check, StringType())

    for x in spark.catalog.listFunctions():
        print(x)

    df2 = dataset1.withColumn("adult",expr("parse_age_function(age)"))

    df2.show()



