for i in range(1,11):
	print(i)
 
 i=1
 while i <= 10:
    print i
    i +=1

a=10
b=20

if a < b:
    print("{} is less then {}".format(a,b))
elif a == 20:
    print("{} is equal to {}".format(a,b))
else:
    print("{} is greater than {}".format(a,b))
    
import os, glob 
os.chdir("/users/sites/")
for file in glob.glob("*.jpg")
    print(file)
   
   
for num in xrange(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print "FizzBuzz"
    elif num % 3 == 0:
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    else:
        print num
        
#range() this returns a range object (a type of iterable)
#xrange() returns the generator object that can be used to display numbers only by looping. the only perticular range is displayed on demand and hence
#called lazy evaluation

# Fibonacci Seqence - previus two numbers added

a,b = 0,1
for i in range(0,10):
    print a
    a,b = b, a + b
    
# Fibonacci Generator
# yield is the keyword we use to make it a generator
# xrange yields one result at a time so we dont overload memory
# range puts the entire range of numbers into the memory at once
def fib(num):
    a,b = 0,1
    for i in xrange(0, num):
        yield "{}: {}".format(i+1, a)
        a,b = b, a + b 
for item in fib(10):
    print item

#Lists
my_list = [10,20,30,40,50]
for i in my_list:
    print i


#Tuples
my_tup = (1,2,3,4,5,6,7,8,9,10)
for i in my_tup:
    print i
    
#Dict - Hash table
my_dict = {'name': 'Bronx', 'age': '2', 'occupation': 'Engineer'}

for key, val in my_dict.iteritems():
    print("{} is {}".format(key,val)
    
#items() - will put all of the objects into memory once
#iteritems() - will put one objects into memory once
    
#set - values will not be repeated
my_set = {10,20,30,40,50,10,20,30,40,50}
for i in my_set:
    print i

set does not guarantee the order, but list does do.

a list may have duplicate elements, but a set may not.
    
Tuples are fixed size in nature whereas lists are dynamic
in other words, a tuple is immutable whereas a list is immutable
can't add elements to tuple, Tuples have no append or extend method
can't remove elements from tuple. tuples have no remove or pop method
you can find elements in a tuple, since this change the tuple
you can also use the in operator to check if element exists in the tuple


Tuples are faster than list

tuples are generally used where order and position is meaningful and constant.

must it be mutable? use a list. Must it not be mutable? use a tuple

otherwise, its a question of choice

for collections of heterogeneous objects (like a address broken into name, street, city,state and zip) I prefer to use a tuple.

likewise, if the collection is going to be iterated over, I prefer a list.

if its just a container t hold multiple objects as one, I prefer a tuple.

#List comprehension

my_list = [1,2,3,4,5,6,7,8,9,10]
squares = [num*num for num in my_list]
print squares

5 Common mistakes
==================

Indentation
module imports - we sometime give module name(python file) same as python standard library

#first class functions

here f is variable
def square(x):
    return x * x
f = square(5)

print(square) //function square at 0X75654
print(f) //25

here variable f is a function 
def square(x):
    return x * x
    
f = square

print(square) //function square at 0X75654
print(f) //function square at 0X79433
print(f(5)) //25

if a function accepts other function as as its arguments or return function as its results thats when we call it as a higher order function

# decorators
dynamically alter the functionality of functions
