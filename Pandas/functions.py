# assign function to a variable

def square(x):
    return x * x


f = square
print(square)
print(f)
print(f(5))


# default args

def hell_func(greeting, name='Kiran'):
    print('{} {}'.format(greeting, name))


# hell_func('Hi how are you,','Murali')
hell_func('Hi how are you,')


# passing list as an arg

def my_function(food):
    for x in food:
        print(x)


fruits = ['Apple', 'Mango', 'Orange']
my_function(fruits)


# variable number of args
# args return the tuple
# kwargs returns the dict
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('math', 'Art', name='John', age=22)


# or

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'Age': 22}
student_info(courses, info)
student_info(*courses, **info)


# functions with no args

def greet():
    print("Welcome to the function")
    c = 2 + 5
    print(c)


greet()


# first_nane and last_nane are the parameters are inputs
# args are the actual values we supply to parameters
# Kiran and Guntur are the arguments


def greet(first_name, last_name):
    print('Hello ' + first_name)
    print('How are you ' + last_name)


greet('Kiran', 'Guntur')


# function does two type of things

# do some task
# output of this function goes to the console


def greet(name):
    print(f"Hi {name}")


greet('Kiran')


# return something

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting('Kumar')
print(message)


# keyword args

def increment(number, by):
    return number + by


print(increment(2, by=1))


# here by = 1 is the keyword arg


# default args
# default parameters should be at the end and all required parameters should be at the begining

def increment(number, by=1):
    return number + by


print(increment(2))


# variable number of args

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 5))


# **args

def save_users(**user):
    print(user["id"])


save_users(id=1, name="Kiran", age=22)


# scope
# here both name and msg are local to the greet function - local variables

def greet(name):
    msg = "a"


# print(msg)
# print(name)

message = "a"


def send_email(name):
    global message
    message = "b"


send_email('Kiran')
print(message)


# pass function as an arg

def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    greeting = func("Hi, I am created by  a function passed as an argument")
    print(greeting)


greet(shout)
greet(whisper)
