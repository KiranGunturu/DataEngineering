from sys import stdin
from pyspark import SparkContext

if __name__ == "__main__":

    sc = SparkContext("local[*]","reduceAndGroupByExample")

    sc.setLogLevel("ERROR")

    baseRDD = sc.textFile("/Users/kirangunturu/Documents/WEEK10-SPARK/bigLog.txt")

    results = baseRDD.map(lambda x: (x.split(":")[0],x.split(":")[1])).groupByKey().map(lambda x: (x[0],len(x[1]))).collect()

    for i in results:
        print(i)

    #stdin.readline()