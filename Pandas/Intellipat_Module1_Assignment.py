# Assignment 1

x=10
y=12
if x>y:
    print(x,"is greater ")
else:
    print(y,"is greater")


# Assignment 2

a,b,c = input("enter three numbers to check the largest:").split()
int(a)
int(b)
int(c)

if a>=b and a>=c:
    largest = a
elif b>=a and b>=c:
    largest = b
else:
    largest = c
print(largest)

# Assignment 3

i=1
while(i<=10):
    print(i)
    i+=1
    
    
# Assignment 4

list=[10,23,4,26,4,75,24,54]
num=0
while num < len(list):
    if list[num] % 2 == 0:
        print(list[num], end=" ")
    num+=1
    
