# Decorators
    # Code readability 
    # A decorator in Python is a function that takes another function as its argument, and returns yet another function. 
    # Decorators can be extremely useful as they allow the extension of an existing function, without any modification to the original function source code.

def square_numbers(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

def cube_numbers(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


## example to calculate exe time of each function
import time

def square_numbers(numbers):
    start = time.time()
    result = []
    for number in numbers:
        return result.append(number*number)
    end = time.time()
    print("square function took str((start-end)*1000) + "milli secs")
    return result


def cube_numbers(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end = time.time()
    print("cube function took str((start-end)*1000) + "milli secs")
    return result
    
array = range(1,10)
out_square = square_numbers(array)
out_cube = cube_numbers(array)

#with decorators

import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + "function took" + str((start-end)*1000) + "milli sec")
        return result
    return wrapper

@time_it
def square_numbers(numbers):
    result = []
    for number in numbers:
        return result.append(number*number)
    return result

@time_it
def cube_numbers(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


array = range(1,10)
out_square = square_numbers(array)
out_cube = cube_numbers(array)


    