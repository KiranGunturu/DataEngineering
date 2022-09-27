x=input("enter your first number: ")
y=input("enter your second number: ")
try:
    #z= x / int(y) to replicate typeError Exception
    z= int(x) / int(y)
except ZeroDivisionError as e:
    print("Devision by zero exception")
    z = None
except TypeError as e:
    #print("exception type: ",type(e).__name__) # to findout what type of exception it is.
    print("TypeError Exception")
    z = None
print("Division is: ",z)