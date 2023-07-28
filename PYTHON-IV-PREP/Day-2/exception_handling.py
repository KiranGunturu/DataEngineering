print(1)
# a = 1/0
print(2)
try:
    a = 1 / 0
except Exception as e:
    print(e)
else:
    print('this is else block')
finally:
    print("this is finally block")
    # ex: closing the database connection which we should do irrespective of exception is there or not
