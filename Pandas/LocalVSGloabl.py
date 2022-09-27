#Global Variable vs local variable#
#Global variable-
total=0
#--------


def sum(a, b):
    print("a:",a)
    print("b:",b)
    #local variable#
    total=a+b
    #---------
    print("total inside the function is:",total)

n=sum(5,6)

print("total sum is:",total)

#----------

