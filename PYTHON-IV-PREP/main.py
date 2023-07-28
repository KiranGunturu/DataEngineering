a = "stallings"
print(a)
print(type(a))

# strings
# numbers / floating
# boolean

# strings

city = 'stallings'
print(city[0])
print(city[4])
print(city[:-1])
print(city[:-2])
print(city[0:4])
print(len(city))
print(city[::-1])

# strings are immutable

print(city.upper())

city = city.upper()
print(city)

city = city.lower()
print(city)

city = city.startswith('st')
print(city)

l1 = [1, 2, 3]
l2 = [3, 4, 5]

print(id(l1))
print(id(l2))

l1 = l2

print(id(l1))
print(id(l2))
print(l1)
print(l2)

str1 = 'I am Kiran'
str2 = 'I live in NC'

print(str1 + ' ' + str2)


f_name = 'kiran'
l_name = 'Gunturu'
age = 30
print(f_name + ' ' + "Hello")
print(f"{f_name} {l_name} lives in NC")
print(f"{f_name} is age is {age}")

company = input()
print(f"I work in {company}")

f_name = 'hello \n'
print(f_name*2)


f = 12.1
print(int(f))

g = '12.1'
print(int(g)) # string to integer is not possible as there will be loss of data

g = '12.1'
print(int(float(g)))


# dynamically typed

# ex: data types are assigned at run time, and we don't need to assign the data types explicitly when we declare them

