//create spark streaming context
val ssc = new StreamingContext(sc, Seconds(5)) / create RDD for every 5 secs
// lines is a dstream
val lines = ssc.socketTextSteam("localhost",9998)

ssc.checkpoint(".") /creates the checkpoint dir in the current working dir
//transformed DStream

def summaryFuct(x: String, y: String) = {
	(x.toInt + y.toInt).toString()
}

def inverseFuct(x: String, y: String) = {
	(x.toInt - y.toInt).toString()
}

val wordCounts = lines.reduceByKeyAndWindow(summaryFuct,inverseFuct, Seconds(10), Seconds(2))
wordCounts.print()
ssc.start()
ssc.awaitTermination()