from pyspark import SparkContext
from sys import stdin

sc = SparkContext("local[*]","loglevelcount")

sc.setLogLevel("ERROR")

if __name__ == "__main__":


    mylist = ["WARN: Tuesday e september 0405",
              "WARN: Tuesday e september 0405",
              "WARN: Tuesday e september 0405",
              "ERROR: Tuesday e september 0405",
              "ERROR: Tuesday e september 0405",
              "ERROR: Tuesday e september 0405"]

    print(mylist)

    originalRdd = sc.parallelize(mylist)

    new_pair_rdd = originalRdd.map(lambda x: (x.split(":")[0], 1))

    reduceRDD = new_pair_rdd.reduceByKey(lambda x, y: (x + y))

    results = reduceRDD.collect()

    reduceRDD.count()

    for i in results:
        print(i)

else:
    print("inside else block")

stdin.readline()