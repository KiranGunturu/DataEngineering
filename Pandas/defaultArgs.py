# default args--



total=0
#--------


def sum(a, b=0):
    print("a:",a)
    print("b:",b)
    #local variable#
    total=a+b
    #---------
    print("total inside the function is:",total)

n=sum(5,8)

print("total sum is:",total)