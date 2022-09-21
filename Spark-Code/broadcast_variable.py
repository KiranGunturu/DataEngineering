import sys
from pyspark import SparkContext

if __name__ == "__main__":

    sc = SparkContext("local[*]","broadcast")

    initialrdd = sc.textFile("/Users/kirangunturu/Documents/WEEK10-SPARK/boringwords.txt")

    results = initialrdd.collect()
    
    for i  in results:
        print(i)




