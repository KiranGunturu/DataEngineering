# using reduce and lambda

from functools import reduce
My_list = ['Hello', 'Welcome to DE']
res = reduce(lambda x,y: x if len(x) > len(y) else y, My_list)
print(res)

# using max+ and len

My_list = ['Hello', 'Welcome to DE']
res = max(My_list, key = len)
print(res)