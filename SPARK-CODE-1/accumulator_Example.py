from sys import stdin
from pyspark import SparkContext


def blanklinechecker(line):
    if(len(line) == 0):
        myaccumulator.add(1)

if __name__ == "__main__":
    sc = SparkContext("local[*]", "blanklinesmyaccumulator")

    sc.setLogLevel("ERROR")

    initialrdd = sc.textFile("/Users/kirangunturu/Documents/WEEK10-SPARK/samplefile.txt")

    myaccumulator = sc.accumulator(0)

    initialrdd.foreach(blanklinechecker)

    print(myaccumulator.value)

    #stdin.readline()


# we can use foreach on a rdd but not on local variable ex list
