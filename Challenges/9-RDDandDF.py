
#### RDD TO DF####

Defineschema=StructType([
        StructField("countryone",StringType(),True),
        StructField("countrytwo",StringType(),True),
        StructField("count",StringType(),True)
        ])


newrows = [
    row("India","USA",1),
    row("pak","UK",1)
        ]
        

parallerrows=spark.sparkContext.parallelize(newrows)

type(parallerrows)

pysparkl.rdd.RDD

newDF=spark.createDataFrame(parallerrows,Defineschema)

type(newDF)

pyspark.sql.dataframe.DataFrame



######### DataFrame to RDD #####


rdd2=rdd.newDF


type(rdd2)

pysparkl.rdd.RDD



    