from pyspark import SparkContext
from sys import stdin

if __name__ == "__main__":
    sc = SparkContext("local[*]", "wordcount")
    sc.setLogLevel("ERROR")
    input = sc.textFile("/Users/kirangunturu/Documents/WEEK9-SPARK/search_data.txt")

    #input = sc.textFile("file:///home/gunturu/file.txt") - file is in local not in hdfs

    # hello how are you hello are you
    words = input.flatMap(lambda x: x.split(" "))
    #hello
    #how
    #are
    #you
    #hello
    #are
    #you
    wordCounts = words.map(lambda x: (x,1))
    #(hello,1)
    #(how,1)
    #(are,1)
    #(you,1)
    #(hello,1)
    #(are,1)
    #(you,1)

    finalCount = wordCounts.reduceByKey(lambda x,y : (x+y))

    # (hello,1)
    # (hello,1)
    # (how,1)
    # (are,1)
    # (are,1)
    # (you,1)
    # (you,1)

    #and then it does following

    # (hello,2)
    # (how,1)
    # (are,2)
    # (you,3)

    results = finalCount.collect()
    # we can save this result to file too as collect will get everything on screen
    finalCount.saveAsTextFile("/Users/kirangunturu/Documents/WEEK9-SPARK/wordcountop.txt")

for a in results:
    print(a)
else:
    print("outside of main function")

stdin.readline()



