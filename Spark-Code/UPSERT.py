from sys import stdin
from pyspark import SparkContext
from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import row_number
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, DateType

if __name__ == "__main__":

    # spark session
    spark = SparkSession.builder \
                        .appName("upsert code") \
                        .master("local[*]") \
                        .enableHiveSupport() \
                        .getOrCreate()
    # set Loglevel
    spark.sparkContext.setLogLevel("ERROR")

    # History Dataframe Creation
    historyData = ([
        [1,'Sean','BA',20000.0,'08-30-2022'],
        [2,'Bella','PM',30000.0,'08-30-2022'],
        [3,'Ross','DA',40000.0,'08-30-2022']
    ])

    # Attach schema

    schema = StructType([
        StructField("emp_id",IntegerType()),
        StructField("emp_name", StringType()),
        StructField("department", StringType()),
        StructField("emp_salary", FloatType()),
        StructField("emp_join_date", StringType())
        ]
    )

    HDF = spark.createDataFrame(historyData,schema)

    HDF.show(truncate=False)

    # HDF.printSchema()
    # Incremental Data
    incData = ([
        [1, 'Sean', 'BA', 20000.0, '08-30-2022'],
        [2, 'Bella', 'PM', 30000.0, '08-30-2022'],
        [3, 'Ross', 'DA', 50000.0, '08-31-2022'],
        [4, 'SAM', 'SM', 60000.0, '09-01-2022'],
        [5, 'MARY', 'MANAGER', 70000.0, '09-02-2022'],
    ])
    # create dataframe and attach schema
    INCDF = spark.createDataFrame(incData,schema)

    INCDF.show(truncate=False)

    # union both HDF and INCDF
    comninedDF = HDF.union(INCDF)
    comninedDF.show(truncate=False)

    # create a window to identify the new and updated records.
    window = Window.partitionBy("emp_id").orderBy(comninedDF["emp_join_date"].desc())
    rankedDF = comninedDF.withColumn("rn",row_number().over(window))
    rankedDF.show(truncate=False)

    # filter the records whose rank is equal to 1
    finalDF = rankedDF.filter(rankedDF['rn'] == 1).drop("rn")

    finalDF.show(truncate=False)

    # write the finalDF results to either HDFS, S3 etc

    finalDF.write \
            .format("csv") \
            .option("path","/Users/kirangunturu/Documents/WEEK12-SPARK/UPSERT/Employee/") \
            .mode("overwrite") \
            .save()




