from pyspark.sql import *
from datetime import datetime, date
import pandas as pd

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("CreatingDataFramesDemo") \
        .getOrCreate()

    df1 = spark.range(5)
    df1.printSchema()
    df1.show()

    data_list = [(1, 2., 'string1', date(2022, 1, 1), datetime(2022, 1, 1, 12, 0)),
                 (2, 3., 'string2', date(2022, 2, 1), datetime(2022, 1, 2, 12, 0)),
                 (3, 4., 'string3', date(2022, 3, 1), datetime(2022, 1, 3, 12, 0))]
    df1 = spark.createDataFrame(data_list).toDF("a", "b", "c", "d", "e")
    df1.show()
    df1.printSchema()

    schema_1 = ['a', 'b', 'c', 'd', 'e']
    schema_2 = 'a int, b double, c string, d date, e timestamp'

    spark.createDataFrame(data_list, schema_1).printSchema()
    spark.createDataFrame(data_list, schema_2).printSchema()

    row_list = [Row(a=1, b=2.0, c='string1', d=date(2022, 1, 1), e=datetime(2022, 1, 1, 12, 0)),
                Row(a=2, b=3.0, c='string2', d=date(2022, 2, 1), e=datetime(2022, 1, 2, 12, 0)),
                Row(a=4, b=5.0, c='string3', d=date(2022, 3, 1), e=datetime(2022, 1, 3, 12, 0))]
    spark.createDataFrame(row_list).printSchema()

    pd_df = pd.DataFrame({'a': [1, 2, 3],
                          'b': [2.0, 3.0, 4.],
                          'c': ['string1', 'string2', 'string3'],
                          'd': [date(2022, 1, 1), date(2022, 2, 1), date(2022, 3, 1)],
                          'e': [datetime(2022, 1, 1, 12, 0), datetime(2022, 1, 2, 12, 0), datetime(2022, 1, 3, 12, 0)]})
    spark.createDataFrame(pd_df, schema_2).printSchema()

    rdd = spark.sparkContext.parallelize([(1, 2.0, 'string1', date(2022, 1, 1), datetime(2022, 1, 1, 12, 0)),
                                          (2, 3.0, 'string2', date(2022, 2, 1), datetime(2022, 1, 2, 12, 0)),
                                          (3, 4.0, 'string3', date(2022, 3, 1), datetime(2022, 1, 3, 12, 0))])
    spark.createDataFrame(rdd, schema_1).printSchema()

