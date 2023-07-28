try:
    f = open("/Users/kirangunturu/Documents/WEEK12-SPARK/biglog.txt", 'r')
    if f.name == 'biglog.txt':
        raise Exception
except FileNotFoundError:
    print("Sorry. File does not exist")
except Exception:
    print('Sorry, Something went wrong')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally")
# finally runs regardless of there is an exception or not ex: close the db connection
# raise is used for custom exception


x = input("enter number1:")
y = input("enter number2:")
try:
    #z = int(x) / int(y)
    z = x / int(y)
except ZeroDivisionError as e:
    print(e)
    z = None
    print("Division is:",z)
except TypeError as e:
    print("Type exception: entered sting instead int")
except ValueError as e:
    print("Value exception")
except Exception as e:
    print("error type is:",type(e).__name__)
    z = None






