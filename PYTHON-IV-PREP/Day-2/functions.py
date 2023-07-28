def greet():
    print("GM")


greet()


def sum_of_two(a, b):
    return a + b


print(sum_of_two(1, 2))


# print(sum_of_two(1))  # error will come as we are not passing all args


# make something default
def sum_of_two(a, b=1):
    return a + b


print(sum_of_two(1))

# global variable

num = 4


def sum_of_two(a, b):
    num = a + b
    return num


print(sum_of_two(1, 5))  # 6
print(num)  # 6


# sum of 3

def sum_of_3(a, b, c):
    num = a + b + c
    return num


print(sum_of_3(1, 2, 3))  # 6


# dynamic no of args
# return type is tuple

def getsum3(*args):
    print(args, type(args))
    num = 0
    for i in args:
        num = num + i
    return num


print(getsum3(1, 2, 3, 4))


# keyword args
# return type is dict when you are not using individual elements like a and b

def getsum(a, b):
    print(a, b)
    print(type(a))
    print(type(b))


print(getsum(b=1, a=2))


def getsum3(**kwargs):
    print(kwargs, type(kwargs))
    print('name', kwargs['name'])


getsum3(id=12, name='Rahul', sal=10000.0)

# __init__.py - tells python that your folder is a package when we have a folder with multiple py files in it
# from mypackage.calc as c (mypackage is folder and calc is a .py file)
# from mypackage.calc import mgetsum (mypackage is folder and calc is a .py file and mgetsum is a function in it)

import pandas as pd
