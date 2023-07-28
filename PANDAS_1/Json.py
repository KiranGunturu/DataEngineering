# import json
# book = {}
# book['tom']={
#     'name' : 'tom',
#     'address' : '1 Gillespeie dr',
#     'phone' : 3446546
# }
#
# book['bob']= {
#     'name' : 'bob',
#     'address' : '24 Green st',
#     'phone' : 34334
# }
#
# s=json.dumps(book)
# print(s)
# with open("C:/Users/kgunturu/Desktop/Python/book.txt","w") as f:
#     f.write(s)

#--------------

f=open("C:/Users/kgunturu/Desktop/Python/book.txt","r")
s=f.read()
print(s)
print(type(s))
import json
book=json.loads(s)
print(type(book))


print(book['bob'])

print(book['bob']['phone'])

for person in book:
    print(book[person])


