import sys
from pyspark import SparkContext

if __name__ == "__main__":

    sc = SparkContext("local[*]","bigdata_Capmaign")

    initialrdd = sc.textFile("/Users/kirangunturu/Documents/WEEK10-SPARK/bigdatacampaigndata.csv")

    mappedrdd = initialrdd.map(lambda x : (float(x.split(",")[10]),x.split(",")[0]))

    #inout
    #big data contents 24.06
    #learning big data 24.06

    #output
    #(big,24.06)
    #(data,24.06)
    #(contents,24.06)
    #(learning,24.06)
    #(big,24.06)
    #(data,24.06)

    flattenrdd= mappedrdd.flatMapValues(lambda x : x.split(" "))

    finalmapped = flattenrdd.map(lambda x : (x[1].lower(),x[0]))

    #finalmapped.collect()

    total = finalmapped.reduceByKey(lambda x,y : (x+y))

    sortedresults = total.sortBy(lambda x : x[1],False)

    results = sortedresults.take(20)

    for i in results:
        print(i)




