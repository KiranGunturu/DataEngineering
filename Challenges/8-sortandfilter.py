###sort vs filter

scenarion 1:

df=spark.read.csv('file.csv)
|
df1.filter("x")
|
df2=df1.sort("y")
|
df2.count()

explain plan : file scan csv - filter - sort

scenarion 2:

df=spark.read.csv('file.csv)
|
df1.sort("x")
|
df2=df1.filter("y")
|
df2.count()

explain plan : file scan csv - filter - sort

scenarion 3:

df=spark.read.csv('file.csv)
|
df.cache()
|
df1.filter("x")
|
df2=df1.sort("y")
|
df2.count()

explain plan : file scan csv -inmemory - filter - sort

scenarion 4:

df=spark.read.csv('file.csv)
|
df.cache()
|
df1.sort("x")
|
df2=df1.filter("y")
|
df2.count()

explain plan : file scan csv -inmemory - filter - sort

out of all four scenarios , scenearion one took less time compare to others.