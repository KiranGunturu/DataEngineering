#lets calculate word count in entire stream and make this as stateful

#updateStateByKey is a stateful transformation we can think of using.

#this requires 2 steps:

#1. Define a state to start with.
#2. a function to update the state

#create spark streaming context
val ssc = new StreamingContext(sc, Seconds(5)) #create RDD for every 5 secs
#lines is a dstream
val lines = ssc.socketTextSteam("localhost",9998)
#creates the checkpoint dir in the current working dir
ssc.checkpoint(".") 
#fun to do operation on entire stream
def updatefunc(newValues:Seq[Int], previousState: Option[Int]): Option[Int] = {
	val newCount = previousState.getOrElse(0) + newValues.sum
	Some(newCount)
#split the words
val words = lines.flatMap(x => x.split(" ")
# map each element and assing the count value
val pairRDD = words.map(x => (x,1))

#ex: data cming as below

#big data is interesting big data is fun

val words = lines.flatMap(x => x.split(" ")
big
data
is
interesting
big
data
is
fun

val pairRDD = words.map(x => (x,1))
(big,1)
(data,1)
(is,1)
(interesting,1)
(big,1)
(data,1)
(is,1)
(fun,1)

then it goes for sorting
(big,1)
(big,1)
(data,1)
(data,1)
(fun,1)
(interesting,1)
(is,1)
(is,1)

(big,{1,1})
(data,{1,1})
(fun,{1})
(interesting,{1})
(is,{1,l})



val wordCounts = pairRDD.updateStateByKey(updatefunc)

rdd1

(big,{1,1}) newValues = {1,1} 2 previousState = 0, (big,2)
(data,{1,1}) newValues = {1,1} 2 previousState = 0, (data,2)
(fun,{1}) (fun,1)
(interesting,{1}) (interesting,1)
(is,{1,1})  (is,2)

rdd2
big data is vast

big
data
is
vast

(big,1) newValues = {1} previousState = 2, (big,3)
(data,1) newValues = {1} previousState = 2, (data,3)
(is,1) newValues = {1} previousState = 2, (is,3)
(vast,1) newValues = {1} previousState = 0, (vast,1)

wordCounts.print()
ssc.start() //starting the streaming application

when we talk about stateful transformation then we have to do checkpointing.



