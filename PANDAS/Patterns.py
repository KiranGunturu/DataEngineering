# Pattern 1

# # # #
# # # #
# # # #
# # # #

for row in range(4):
    for col in range(4):
        print("# ",end="")
    print("\n")
    
# Pattern 2
# Hint - No of columns is eqaul to row number

# 
# # 
# # #
# # # #
# # # # #


number=int(input("enter your number:"))
for row in range(1,number+1):
    for col in range(row):
        print("# ",end="")
    print("\n")
    
# Pattern 3
#Hint - No of columns are decreasing when row number increases.

# # # # #
# # # #
# # #
# #
#

number=int(input("enter your number:"))
for row in range(number,0,-1):
    for col in range(1,row+1):
        print("# ",end="")
    print("\n")
    
# Pattern 4
#Hint - Combination of pattern 2 and 3

# 
# # 
# # #
# # # #
# # # # #
# # # #
# # # 
# #
#

number=int(input("enter your number:"))
for row in range(1,number+1):
    for col in range(1,row+1):
        print("# ",end="")
    print("\n")
#number=int(input("enter your number:"))
for row in range(number-1,0,-1):
    for col in range(1,row+1):
        print("# ",end="")
    print("\n")



# Pattern 5
# Hint - print the corresponding row values

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

number=int(input("enter your number:"))
for row in range(1,number+1):
    for col in range(1,row+1):
        print(row,end=" ")
    print("\n")

# Pattern 6
# Hint - print the corresponding col values

1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5


number=int(input("enter your number:"))
for row in range(1,number+1):
    for col in range(1,row+1):
        print(col,end=" ")
    print("\n")

# Pattern 7


1 

1 2 

1 2 3 

1 2 3 4 

1 2 3 4 5 

1 2 3 4 

1 2 3 

1 2 

1 


number=int(input("enter your number:"))
for row in range(1,number+1):
    for col in range(1,row+1):
        print(col,end=" ")
    print("\n")
for row in range(number-1,0,-1):
    for col in range(1,row+1):
        print(col,end=" ")
    print("\n")
    
    
# Pattern 8

11 

12 22 

13 23 33 

14 24 34 44 

15 25 35 45 55 


number=int(input("enter your number:"))
for row in range(1,number+1):
    for col in range(1,row+1):
        print("{0}{1}".format(col,row),end=" ")
    print("\n")


# Pattern 9

11 

21 22 

31 32 33 

41 42 43 44 

51 52 53 54 55 

number=int(input("enter your number:"))
for row in range(1,number+1):
    for col in range(1,row+1):
        print("{0}{1}".format(row,col),end=" ")
    print("\n")


# Pattern 10


11 

21 22 

31 32 33 

41 42 43 44 

51 52 53 54 55 

41 42 43 44 

31 32 33 

21 22 

11 



number=int(input("enter your number:"))
for row in range(1,number+1):
    for col in range(1,row+1):
        print("{0}{1}".format(row,col),end=" ")
    print("\n")

#number=int(input("enter your number:"))
for row in range(number-1,0,-1):
    for col in range(1,row+1):
        print("{0}{1}".format(row,col),end=" ")
    print("\n")
    

# Pattern 11

1 

2 3 

4 5 6 

7 8 9 10 

11 12 13 14 15 

number=int(input("enter your number:"))
sum=0
for row in range(1,number+1):
    for col in range(1,row+1):
        sum+=1
        print("{0}".format(sum),end=" ")
    print("\n")

# Pattern 12
# Best Alternative solution for # Pattern 2 

    #### Increasing traingle ###



n=5
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
* 
* * 
* * * 
* * * * 
* * * * * 

# explanation
# outer for loop wil give 5 rows
# 0:i=0+1 (inner for loop) so in the first run it gave us one star  *
# 1:i=1+1 (inner for loop) so in the first run it gave us two stars * *
#etc
# 
i=0 * 
i=1 * * 
i=2 * * * 
i=3 * * * * 
i=4 * * * * * 

# Pattern 13
# Best Alternative solution for # Pattern 3

    #### Decreasing traingle ###
    
* * * * * 
* * * * 
* * * 
* * 
* 

# explanation
# outer for loop wil give 5 rows

i=0* * * * * 
i=1* * * * 
i=2* * * 
i=3* * 
i=4* 

0 to 5* * * * * 
1 to 5* * * * 
2 to 5* * * 
3 to 5* * 
4 to 5* 

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

# Pattern 14
# right traingle
# combination of decreasing traingle with space and increased traingle with *

          * 
        * * 
      * * * 
    * * * * 
  * * * * * 

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

# Pattern 15

# left traingle
# combination of increased traingle with space and decreasing traingle with *

  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
          
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    #print()
    for j in range(i,n):
        print("*",end=" ")
    print()

# Pattern 16

# Hill Pattern

# combination of decreasing traingle with space and two increased traingle of star

          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end= " ")
    print()

# Pattern 17

# Reverse Hill Pattern
# combination of increased traingle of space and two decreasing traingle of star

   * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
 
 
 # Pattern 18
 
 #Diamond pattern
 
 # combination of hill and reverse hill partition but reducing one iteration in the outer for loop(n-1)
  
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
 n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end= " ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

# Pattern 19

# Pyramid
# hint is : increased traingle with prinint spaces 

    * 
   * * 
  * * * 
 * * * * 
* * * * *

n=5
for i in range(n):
    for j in range(number-i-1):
        print(end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
 
 # Pattern 20
 
 # Left Pascal Traingle 
 # Hint : Combination of Increasing traingle and decreasing traingle
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
 
 n=5
for i in range(n-1):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()


 # Pattern 21
 
 # Right Pascal Traingle 
 # Hint : Combination of decreasing space and increased traingle joined with increased space and decreasing star
 
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
 
 n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
 
 # Pattern 22
 
 # Combination of Hill Pattern and reverse hill pattern
 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
 n=5
for i in range(n-1):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
    
 # Pattern 23
  # Butterfly
  
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
  
  n=5
for i in range(1,n):
    print("*"*i,end="")
    print(" "*(n-i)*2,end="")
    print("*"*i)
for i in range(n,0,-1):
    print("*"*i,end="")
    print(" "*(n-i)*2,end="")
    print("*"*i)
    
# Pattern 24

#Hint - flip the for loops in partition 23



**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
    
n=5
for i in range(n,0,-1):
    print("*"*i,end="")
    print(" "*(n-i)*2,end="")
    print("*"*i)
for i in range(1,n+1):
    print("*"*i,end="")
    print(" "*(n-i)*2,end="")
    print("*"*i)