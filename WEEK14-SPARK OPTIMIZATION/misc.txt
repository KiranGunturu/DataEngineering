1) #####Repartition vs coalesce#####

You have two dataframes df1 and df2, you will need to join both the dataframes and write the output as 5 part files in a optimized way. Would you use coalesce or repartition?

df3 = df1.join(df2,["id"],"inner")

df3.coalesce(5).write.parquet(path) 

or 

df3.repartition(5).write.parquet(path)


Candidate :

By default join will create 200 part files. I will go for coalesce(5) as we need to decrease the part files from (200 to 5) and it avoids full shuffle.


Repartition took :13.40 Mins
coalesce took : 15.14 Mins


Reason - 

If you use coalesce(5), It will enforce the spark.sql.shuffle.partitions value to 5 from 200 and all the join has to perform in 5 partitions.

If you use repartition(5), It preserves the spark.sql.shuffle.partitions value and does the join in 200 partitions.

2) #####Use of RDD vs DF#####

What is the difference between RDD and dataframe ?


RDD is schema less, dataframe has schema
RDD does not have inbuilt optimization, dataframe has catalyst optimizer
RDD can handle structured, unstructured and semi structured data , dataframe can handle only structured and semi structured data.

but the major difference between RDD and dataframe?

RDD occupies 2x space of dataframe in memory.

I have read text file as RDD and dataframe and persisted both using MEMORY_ONLY storage level.

RDD occupied memory- 228 MB
Dataframe occupied memory - 101 MB

-----------

whenever we do shuffling incase of structured API we get 200 partitions by default.

if I do groupBy on a dataframe, then we will get 200 partitions after the shuffling is done.

in a rdd approach, lets say we have 500Mb file

rdd - groupBy then
before groupBy we had 4 partitions
after groupBy the partitions remain the same that means still 4 partitions


3) #####optimize file copy#####

Requirement is to move 65k small files(Each file under 1MB) programmatically from one bucket to another bucket once ETL job is completed.

You tried with AWS Lambda but this keeps failing with timeout error since lambda timeout is 15 mins.

How would you handle this scenario and optimize copy execution time ?

Multiple solutions:

First:
Long term solution trigger an AWS batch job from lambda function which overlooks the process of moving files in one go rather than iterating it out over and over or can do it in micro batches after zipping them.


Second:
write a GLUE ETL Job which does it. but is very costly in terms of resources and budget.


Third:
Use the same lambda function and rather than attempting to write all of them at one go set a trigger for that folder location 
to lambda, capture event of one single file being written in that S3 bucket and process in lambda the same way you are doing. 
This way with standard replication factor of 10k lambda can handle upto 10k files in a go and this would make it completely stateless pluss immune to frequency 
and load and finally solve lambda duration problem.

4)#####MD5#####

You have a target table created out of parquet format with 500 columns and 1B rows and you are receiving 20G incremental data daily from source.

Requirement is to check if the source record exists in target table, If yes ignore the record, if not append the record to target table.

How would you optimize above ask ??

dfSource = dfSource.withColumn("record_hash_key",md5logic")

dfTarget = spark.table("tgtTbl").select("record_hash_key")

dfFinal =

dfSource.alias("src").join(Df Target.alias("tgt"),["record_hash_key"],"left").where("tgt.record_hash_key is null").select(*requiredCols)


dfFinal.write.mode("append").insertInto("tgtTbl")

5)#####Best Join to Avoid shuffle#####
We have 4 spark dataframes n the counts are below.

df1 = 1M rows - Incremental data
df2= History data - 50GB
df3= History data - 100GB
df4 = History data - 200GB

Requirement is to populate the final dataset by joining 4 dataframes, Below is the sample join query.

df1.join(df2,["id"],"inner")\
.join(df3,["type"],"inner")\
.join(df4,["value"],"inner")

How would you optimize above join ??

df1Stg = df2.join(broadcast(df1),["id"],"inner")
df1Stg.cache().count()


df2Stg =df3.join(broadcast(df1Stg),["type"],"inner")

df2Stg.cache().count()

dfFinal =
df4.join(broadcast(df2Stg),["value"],"inner")

If you put all joins in a single query , Spark would go for sort merge join and there would be shuffle. So here the trick is to split the joins n take advantage of Broadcast in every join to avoid complete shuffle. I recently had a requirement to join small table with 42 billion rows ,2 billion rows n 5 billion rows, 
This approach helped me in optimizing the run time..

6)#####cache lineage#####


What would be the output of below code ?

from pyspark.sql.functions import *
df = spark.read.parquet("file1.parquet")
df = df.cache()
df.withColumn("file_name",input_file_name()).select("file_name").distinct().show()

https://stackoverflow.com/questions/56810730/why-is-input-file-name-empty-for-s3-catalog-sources-in-pyspark

he concept of input_file_name does not make sense in this context, given the original file path is no longer a direct input.

since df is cached , the lineage is broken. So file_name column with single record as "NULL" should be the output. 

7)#####Process Large Zip file#####

You are receiving a ZIP file of 10GB from source system and you will have to Unzip and push it to another S3 Bucket for the spark job to read.

You tried with AWS Lambda but its failing with memory error. What else serverless solution you can think of in AWS?

--GLUE

7)#####optimization1#####

We have a parquet file size of 15 GB.

method1 :

df1 = spark.read.parquet("file_name")
df1.count()
df1.filter(col1>10).show()

method2 :

df1 = spark.read.parquet("file_name").cache()
df1.count()
df1.filter(col1>10).show()

Which one run in quick time ?


Method1 :

1) it uses footer to get the count instead of reading all the data

2) it uses column pruning to filter the record .


Method2: 1) First it has to cache the data and it has read all the data from memory cache to get the count instead of taking it from metadata footer.

2) it has to read all the data from memory to filter instead of column pruning

So for columnar files , it's not a good idea to cache the data especially for getting count .

Method1 is fast.

https://towardsdatascience.com/best-practices-for-caching-in-spark-sql-b22fb0f02d34#:~:text=Faster%20than%20caching&text=No%20wonder%20that%20the%20first,to%20reading%20directly%20from%20parquet

8)#####optimization2#####

You have two dataframes with 20 GB each, The requirement is to join these two dataframes and write the output dataframe as single file.

val df3= df1.join(df2,df1("id")===df2("id"),"left")

Which option do you prefer and why ?

Option 1 :
df3.repartition(1).write.save(targetLocation)

Option 2:
df3.coalesce(1).write.save(targetLocation)

The Answer is repartition(1).

If you use coalesce(1), It will enforce the spark.sql.shuffle.partitions to 1 from default 200 and all the join has to perform on single partition.

Since the data is huge, Join can take significant amount of time. With the repartition even though it involves in shuffling, It will still use 200 partitions and does the Join operation in parallel.

There is a POC done with 1.5 GB data, repartition is taking 13 secs while coalesce is taking 17 secs. With the huge data the performance will be even more better with repartition.

https://blog.devgenius.io/a-neglected-fact-about-apache-spark-performance-comparison-of-coalesce-1-and-repartition-1-80bb4e30aae4

9)#####optimization3#####

df1 has 1 billion records - History data
df2 has 10 million records - Incremental data

We need to find out the records which exists in df2 but not in df1.

This can done using inbuilt functions

df3 = df2.exceptAll(df1) or using left anti join.

Do you prefer to go with spark inbuilt functions or Do you have any customized way of doing it to optimize it considering the volume ?

1. Derive column FullRowHash by Calculating Full Row Hash / MD5 of all columns on both DFs except audit columns & timestamps
2. Repartition Both DF -
How = On Natural/Primary Keys
How many partitions = Num Cores multiplied by Num Executors
3. SELECT Natural keys from DF2 only which doesn't match HashCode in DF1 also Natural Keys from DF2 which are new / 1st time appearing - Do UNION ALL.
4. JOIN Step 3 result with DF2 & Select all the columns from DF2

Four steps but super efficient, No OOM, No Container spillage, No Sparse data issue, plus can be a put into a function & reuse the function everywhere this task is required

For fully utilization of resources available configured to that particular spark job, parallelism must be set high enough.
Hence..
1. Too few partitions means not utilizing all available resources.
2. Too many partitions means overhead.
3. Hence we define upper bound, lower bound & a balanced bound.
Num repartitions Upper bound = num executor times num cores
Num repartitions Lower bound = 2 times num cores
Num repartitions Balanced bound = 4 times num cores
Note: To use above formula max num cores must never cross 5 as HDFS do not entertain more that 5 IO threads that's why Max 5 cores.
Example - If we go by 1 core per executor then ultimately parallelism will be num executor times. But if we have more than 1 core per executor there will be threads within executor gives effective throughput.
What happens num cores is > 5 = Bottleneck, linear processing like FIFO

The above 3 cases of repartitioning can be put into IF-ELSEIF-ELSE statement according to parallelism required directly proportional to volume of data.

