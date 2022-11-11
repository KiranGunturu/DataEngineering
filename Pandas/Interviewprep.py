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

when we have memory constraint - tuple
when we know how many columns we will have - tuple
when we dont know how many columns will be and if it is more of dynamic - list

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

tips
====
1)

x = input("give me numbers")
print(x)


x, y = input("give me numbers").split()
print(x)
print(y)

2)

AND Clause
===============
subs = 2400
likes = 200
comment = 56

if(subs > 150 and likes > 150 and commnet > 50):
    print('Awesome Video')

or 

conditions = [subs > 150, likes > 150, commnet > 50]

if all(conditions):
    print('Awesome Video')

3)
   
OR Clause
==========

if(subs > 2500 or likes > 500 or commnet > 50):
    print('Awesome Video')
    
or

checkers = [
            subs > 2500,
            likes > 500,
            commnet > 50
            ]
if any(checkers):
    print('Awesome Video')
    
4)

subs = 2400
likes = 200

print(subs, likes)

temp = subs
subs = likes
likes = temp

print(subs, likes)

or

subs, likes = likes, subs

5) remove dupes

a = [1.3,4,5,7,7,7,4]
print(a)
a = list(set(a))
print(a)


6) most repeated

a = [1.3,4,5,7,7,7,4]
print(a)
most = max(set(a), key=a.count)
print(most)

7) square of odd numbers

odd_squares = []
for i in range(11):
    if i % 2 = 1:
        odd_squares.append(i**2)
print(odd_squares)

or

odd_squares = [ i**2 for i in range(11) if i % 2 == 1 ]
print(odd_squares)

8) variable number of args

def sum(a, b):
    return a + b
 
 res = sum(2, 3)
 print(res)
 
 or 
 
 def sum(*a):
    result = 0
    for i in a:
        result = result + i
    return result
    
res = sum(2, 3, 5, 10)
 print(res)
 
 
 9) reverse the string
 
 name = 'Kiran Kumar'[::-1]
 print(name)
 

 10) Palindrome
 
 name = 'madam'
 isPalindrome = name.find(name[::-1])==0
 print(isPalindrome)
 
 
 11) count number of chars
 
 def count_no_of_chars(s):
    count={}
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

#s=['Hello','Hello','Kiran']
s='Hello'
count_no_of_chars(s)

case sensitive
indentation
interpreted and dynamically typed language
doesn't need to be compiled before run
suite - group of individual statements, which make a single code block
datatypes -
    Int
    float
    dicts
    sets
    lists(arrays)
    tuples
    string
    boolean
ways to concatenate tuple
    tup1 + tup2
    or
    sum(tup1, tup2), ())
    0r
    x= list(tup1)
    y= list(tup2)
    x.extend(y)
    res=tuple(x)
slice operator - print range of elements
different functions

    passing the args to the function in the order they defined
    keyword args - can be specified in any order but should specify name of the keyword
    default args - pass the default values in the fun itself
    
       built-in
       
        print()
        abs()
        dict()
        enumerate()
        max()
        min()
        pow()
      recursive
      
        return (n * calc_fact(n-1))
        
      lambda - Can have any no of parameters but, can have just one statement.
      
        double = lambda x: x * 2
        print(double(5))
        
self - to refer the specific instance of the class
pass - skipping a specific function
check if string starts with digit
    string='1abc'
    string[0].isdigit()
regular expressions - to match any pattern
import re
python keywords

    and
    or
    not
    if
    elif
    else
    for
    while
    break
    as
    def
    lambda
    pass
    return
    true
    false
    try
    with
    class
    continue
    del
    except

python modeules

    os
    sys
    math
    random
    json
    date time
    
array and list
===============

array - hold only single data type elements
list - list can hold any data type elements

__init__ = constructor in python
this method is automatically called to allocate memory when a new object/instance of class is created.
all classes have __init__ method

class Employee:
def __init__(self, name, age,salary):
self.name = name
self.age = age
self.salary = 20000
E1 = Employee("XYZ", 23, 20000)
# E1 is the instance of class Employee.
#__init__ allocates memory for E1. 
print(E1.name) //XYZ
print(E1.age) //23
print(E1.salary) //20000


randomize the items of list -- 
from random import shuffle
x = [1,2,3,4,5]
shuffle(x)

generator - Functions that return an iterable set of items are called generators.

docstring

"""

hello

"""

is - checks wheather two variables point to the same object in memory
== - compares the value wheather two variables point to the same object in memory
not - 
in - 


clousure
==========

clousure in python is an inner function object.
A function that behaves like an object that remembers and has access to variables in the local scope in which it was created even after
    the outer function has finished executing.

def outer_func():
    message = "Hi"
    
    def inner_func():
        print(message)
    return inner_func()

outer_func()

shallow vs deep copy
=====================
shallow copy copies all the reference pointers, all the values but it creates a new original by itself in a seperate memory location
shallow - copy.copy() - faster
deep - copy.deepcopy() - slower

>>> l1 = [1,2,3,4]
>>> l2 = l1
>>> l2.append(10)
>>> l2
[1, 2, 3, 4, 10]
>>> l1
[1, 2, 3, 4, 10]
>>> import copy
>>> l1
[1, 2, 3, 4, 10]
>>> l3 = copy.copy(l1)
>>> l3
[1, 2, 3, 4, 10]
>>> l3.append(11)
>>> l3
[1, 2, 3, 4, 10, 11]
>>> l1
[1, 2, 3, 4, 10]
>>> l2
[1, 2, 3, 4, 10]
>>> id(l1)
139943057024856
>>> id(l2)
139943057024856
>>> id(l3)
139943057201200

list vs tuple
==============
>>> l1
[1, 3, 4, (5, 6)]
>>> l1.append(7)
>>> l1
[1, 3, 4, (5, 6), 7]

in above case we can't modify the tuple though it is inside the list

>>> l3 = ([1,2,3], )
>>> l3
([1, 2, 3],)
>>> l3[0].append(4)
>>> l3
([1, 2, 3, 4],)

ternary operators
==================

>>> x,y = 23,50
>>> big = x if x > y else y
>>> big
50


sort numerical dataset
======================

>>> l1 = ["1","4","2","10","5"]
>>> l1
['1', '4', '2', '10', '5']
>>> l1.sort()
>>> l1
['1', '10', '2', '4', '5']
>>> l1 = [int(i) for i  in l1]
>>> l1.sort()
>>> l1
[1, 2, 4, 5, 10]


or

>>> l2 = ["1","4","2","10","5"]
>>> l2
['1', '4', '2', '10', '5']
>>> l2 = map(int, l2)
>>> l2
[1, 4, 2, 10, 5]
>>> l2.sort()
>>> l2
[1, 2, 4, 5, 10]







    
    

    
    


