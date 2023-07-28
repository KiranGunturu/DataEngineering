import sys
from pyspark import SparkContext

if __name__ == "__main__":

    sc = SparkContext("local[*]", "MovieRatings")

    baseRdd = sc.textFile("/Users/kirangunturu/Documents/WEEK11-SPARK/ratings.dat")

    mappedRdd = baseRdd.map(lambda x: (x.split("::")[1], x.split("::")[2]))

    # input
    # (1194,4)
    # (1193,5)
    # (1193,3)

    # output
    # (1194,(4.0,1.0))
    # (1193,(5.0,1.0))
    # (1193,(3.0,1.0))

    new_mapped = mappedRdd.mapValues(lambda x: ((float(x), 1.0)))

    # input
    # (1194,(4.0,1.0))
    # (1193,(5.0,1.0))
    # (1193,(3.0,1.0))

    # output
    # (1194,(12.0,3.0))
    # reduceByKey - reduce by key and aggregate values

    reduced_rdd = new_mapped.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

    # input
    # (1194,(12000.0,3000.0))
    # x[0] = 1994
    # x[1] = (12000.0,3000.0)
    # x[1][0] = 12000.0

    filtered_Rdd = reduced_rdd.filter(lambda x: x[1][0] > 1000)

    # input
    # (1194,(12000.0,3000.0))

    ratings = filtered_Rdd.mapValues(lambda x: x[0] / x[1]).filter(lambda x: x[1] > 4.5)

    movies_rdd = sc.textFile("/Users/kirangunturu/Documents/WEEK11-SPARK/movies.dat")

    mappedd = movies_rdd.map(lambda x: (x.split("::")[0], x.split("::")[1]))

    joined_rdd = mappedd.join(ratings)

    top_movies = joined_rdd.map(lambda x: x[1][0])

    final_results = top_movies.collect()

    for i in final_results:
        print(i)
