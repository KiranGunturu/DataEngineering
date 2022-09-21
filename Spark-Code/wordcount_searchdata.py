import sys
from sys import stdin
from pyspark import SparkContext

if __name__ == "__main__":
    sc = SparkContext("local[*]","wordcountsearchdata")
    sc.setLogLevel("ERROR")
    #print(sc.version)

    rdd1 = sc.textFile("/Users/kirangunturu/Documents/WEEK9-SPARK/search_data.txt")
    rdd2 = rdd1.flatMap(lambda x : x.split(" "))
    rdd3 = rdd2.map(lambda x:(x.lower(),1))
    rdd4 = rdd3.reduceByKey(lambda x,y : (x+y))
    #instead above line we can also do below refer wordcount_program_notes.txt file for explanation
    rdd5 = rdd3.countByValue()

    results = rdd4.collect()

    print(sys.getsizeof(int()))

    for a in results:
        print(a)
