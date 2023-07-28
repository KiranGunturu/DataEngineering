//create spark streaming context
val ssc = new StreamingContext(sc, Seconds(5)) / create RDD for every 5 secs
// lines is a dstream
val lines = ssc.socketTextSteam("localhost",9998)

ssc.checkpoint(".") /creates the checkpoint dir in the current working dir
//transformed DStream
val words = lines.flatMap(x => x.split(" ") 
val pairRDD = words.map(x => (x,1)).reduceByKeyAndWindow((x,y)=>x+y,(x,y)=>x-y, Seconds(10), Seconds(2))
wordCounts.print()
ssc.start()
ssc.awaitTermination()