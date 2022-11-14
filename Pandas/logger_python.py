# https://docs.python.org/3/library/logging.html#logrecord-attributes
# logging.disable - it will disable all the logging statements
# by default log file will be appended. if we want to overwrite use filemode = 'w'
# root (basicConfig)- default logger name
# 10 DEBUG
# 20 INFO
# 30 WARNING
# 40 ERROR
# 50 CRITICAL

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
fh = logging.FileHandler('logger_python.log')
fh.setFormatter(f)
logger.addHandler(fh)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# debug will not give anything to the console


num1 = 10
num2 = 5
add_result = add(num1, num2)
# print('Add: {} + {} = {}'.format(num1, num2, add_result))
logger.debug('Add: {} + {} = {}'.format(num1, num2, add_result))

sub_result = subtract(num1, num2)
# print('sub: {} - {} = {}'.format(num1, num2, sub_result))
logger.debug('sub: {} - {} = {}'.format(num1, num2, sub_result))

multiply_result = multiply(num1, num2)
# print('multiply: {} * {} = {}'.format(num1, num2, multiply_result))
logger.debug('multiply: {} * {} = {}'.format(num1, num2, multiply_result))

divide_result = divide(num1, num2)
# print('divide: {} / {} = {}'.format(num1, num2, divide_result))
logger.debug('divide: {} / {} = {}'.format(num1, num2, divide_result))
