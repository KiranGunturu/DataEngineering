# Memory - 1

List1 = [5, 6]
List2 = [5, 6]

print(List1)
print(List2)

print(hex(id(List1)))
print(hex(id(List2)))

List1 = List2

print(List1)
print(List2)


# check if element is in List - 2

def check_element(list3, element):
    if element in list3:
        print("element exists")
    else:
        print("element not exists")


list3 = [1, 2, 3, 'a', 'b', 'c']
element = 'a'
check_element(list3, element)

# how to iterate over multiple lists - 3

name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]

z = zip(name, animal, age)

for name, animal, age in z:
    print("%s the %s is %s" % (name, animal, age))

# is list mutable - 4

x = [1, 2]
x.extend([5])
print(x)
x.append([6, 7])
print(x)
x.extend([8, 9])
print(x)

# is list need to be homogeneous - 5

x = [1, 1.0, 'a', []]
print(x)

# difference between append % extend - 6

x = [1]
x.append(2)
print(x)
x.append([3, 4])
print(x)
x.extend([5, 6])
print(x)

# Do python list store values or pointers? - 7
# Python lists don’t store values themselves.
# They store pointers to values stored elsewhere in memory. This allows lists to be mutable.
# if values are same then they both point to same address

print(id(1))
print(id(2))
a = [1, 2, 3]
print(id(a))
print(id(a[0]))
print(id(a[1]))

# 8. What does “del” do?
# del removes an item from a list given its index.
# del does not return the removed element.

x = [1, 2, 3, 4]
del x[1]
print(x)

# 9. What is the difference between “remove” and “pop”?
# .remove() removes the first instance of a matching object. Below we remove the first b.

x = [1, 2, 3, 4, 4, 5, 6]
x.remove(4)
print(x)
x = ['a', 'b', 'c', 'c', 'd', 'e']
x.pop(4)
print(x)

# The difference between pop and del is that pop returns the popped element. This allows using a list like a stack.
# By default, pop removes the last element from a list if an index isn’t specified.

def countNoOfChars(list):
    count={}
    for i in list:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

list = ['hello','hello','world']
print(countNoOfChars(list))

