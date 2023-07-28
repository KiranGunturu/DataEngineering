marks = 40
if marks < 30:
    print("fail")
    print(f"marks are {marks}")
elif marks >= 30 <= marks < 60:
    print("pass with second division")
elif marks >= 60 and marks <= 75:
    print("pass with first division")
else:
    print("pass with distinction")

# while (infinite loop)
n = 0
while n < 5:
    print("it is still less than 5")
    n=n+1


num = [1,2,3]
num_square = []
n=0
while n < len(num):
    num_square.append(pow(num[n],2))
    n=n+1
print(num_square)

# for loops
num = [1,2,3]
num_square = []
for n in num:
    num_square.append(pow(n, 2))
    print(n)
print(num_square)

# range
for i in range(5):
    print(i)

num_square=[]
for n in range(len(num)):
    num_square.append(pow(num[n],2))

print(num_square)


