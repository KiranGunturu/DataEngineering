Big 0 = way of comparing two sets of code.
===========================================

lets say code1 & code2 accomplish exactly the samething

how would you compare one against the other?

code1 might be more readable

code2 might be more concise

code might only take few lines and faster then code is better

big 0 is comparing code1 and code2 mathematically about how efficient they run.

time complexity
===============

code1 - 15 secs
code2 - 60 secs based on this we say code1 is better and this is called time complexity

but time complexity it is not measured in terms of time because if we run code1 and code2 on different machine where it has more
resources then execution time varies - in this case its not the code is efficient but machine is efficient.

space complexity
================

code1 - 15 secs but takes lot of memory
code2 - 60 secs but it may take less memory

it all depends on what we are trying to solve and based on that our approach differs.

three different things
=======================

Ω (Alt + 234)
Θ (Alt + 233)
O

lets say we have a list 

1 2 3 4 5 6 7

lets say we are looking for 1 then it is our best case scenario - Ω (Omega)
lets say if we are looking for 7 then it is worst case scenario as we have to iterate thru entire list. - Big O
lets say if we are looking for 4 then it is average case scenario - Θ (Theta)


1)

O(n)
======

def print_items(n):
	for i in range(n):
		print(i)


print_items(10)

0
1
2
3
4
5
6
7
8
9

Drop Constants
================

def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
        
print_items(n)

0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9

here it works as n+n and also can be referred as O(2n) but we can simply drop constant and call it as O(n)



def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
            
print_items(3)

https://www.youtube.com/watch?v=shO5VbD2rNI

0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2

this is n * n = n² = o(n²)

def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)
                
print_items(3)

0 0 0
0 0 1
0 0 2
0 1 0
0 1 1
0 1 2
0 2 0
0 2 1
0 2 2
1 0 0
1 0 1
' ' '
' ' '
9 9 9

this is n * n * n = n³ = o(n³)

we will simply this as O(n²) irrespective of sq or cube

this means it is lot less efficient than O(n) from a time complexity stand point.



Drop Non Dominants
====================


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
    
print_items(3)

0 0
0 1
0 2
1 0
1 1
1 2
0
1
2

here nested for loop ran O(n²) and outer loop (k) ran for o(n)

so o(n²) + o(n) = o(n² + n) 



O(1)
========

def add_items(n):
    return n + n
    
 add_items(3)
 9
 even if our n is 1000 then there will be only one operation
 
 O(log n)
 ============
 
 what is the best way to find number 5?
 
 1 2 3 4 5 6 7 8
 
 step 1) 1 2 3 4             5 6 7 8
 
 step 2) 5 6 7 8
 
 step 3) 5 6
 
 it took 3 steps to find the number 5
 
 2³ = 8
 
 is same as log2 8 = 3
 
 log2 1,073,741,824 = 31
 
 we have to cut number 1,073,741,824 into 31 times to get 1 item from the list having more than billion elements.
 
 if we dont use o(log n) then we end up scanning the list close to billion times seqentially.
 
 