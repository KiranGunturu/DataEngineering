# list
# tuple
# dict

# list -
# mutable
# dupes are allowed
# elements can be of diff type

IPL = ['CSK', 'MI', 'RCB', 'LSG']
print(type(IPL))
# indexing
print(IPL[0])
# slicing
print(IPL[0:])
print(IPL[0:3])
print(IPL[:-1])

IPL[1] = 'KKR'
IPL.append('MKR')  # at the end of the list
IPL.insert(2, 'MI')  # insert at the second index and move all to the right
IPL.extend([1, 2])  # add at the end as an individual elements like 1,2
IPL.insert(1, [1, 2])  # add at the index 1 as a list
print(IPL)
print(IPL[0][0:2])  # CS
print(IPL[0][0:2].lower())  # cs
IPL.pop()  # always deletes the last element and returns the deleted element as output
IPL.pop(2)  # deletes the second element in a list and returns the deleted element as output
# method 1 to create list
a = []  # empty list
a.append(2)
a.append([3, 4])  # add at the end as a list
print(a)
# method 2 to create list
ipl_string = "CSK,MI,KKR,LSG"
ipl_list = ipl_string.split(",")  # converts above string as a list
print(ipl_list)
# method 3 to create list
python_list = list('Hello')
print(python_list)

# sorting
l1 = [1, 2, 4, 3, 5]
l1.sort()  # by default asc order
print(l1)
l1.sort(reverse=True)  # desc order
print(l1)

# list of list

list_of_list = [[1, 2], [2, 4], ['Hello', 'world']]
print(len(list_of_list))
print(list_of_list[0][0])  # 1
print(list_of_list[0][1])  # 2
print(list_of_list[2][1][2])  # r (second list, first element and 2nd index)

# copy the list

ipl_new = IPL # now both the lists will point to same memory location so if we make changes to one list then it will impact the other list too
print(ipl_new)

ipl_copy = IPL.copy() # now both the lists are pointing to diff location


# when both lists pointing to same address
# here the changes are happening to both the lists

a = [1,2,3]
b = [2,3,4]
b=a
print(a) #[1,2,3]
print(b) #[1,2,3]

a = [1,2,3]
b = [2,3,4]
a=b
print(a) #[2,3,4]
print(b) #[2,3,4]
a.pop()
print(a) #[2,3]
print(b) #[2,3]

# here we copied c into d and if we make changes to c then those will not be impacted to d

c = [1,2,3]
d = c.copy()
print(d) #[1,2,3]
c.pop()
print(c) #[1, 2]
print(d) #[1, 2, 3]

# shallow copy (when we have nested list, those lists will point to same address location
e = [[1,2],[3,4]]
f = e.copy()
print(e) # [[1, 2], [3, 4]]
print(f) # [[1, 2], [3, 4]]
f.pop()
print(e) # [[1, 2], [3, 4]]
print(f) # [[1, 2]]

print(f[0][0]) #1
f[0][0]=2
print(e) # [[2, 2], [3, 4]]
print(f) # [[2, 2]]

# deep copy (two lists will not point to the same location)
import copy
e = [[1,2],[3,4]]
f = copy.deepcopy(e)
print(e) # [[1, 2], [3, 4]]
print(f) # [[1, 2], [3, 4]]
f.pop()
print(e) # [[1, 2], [3, 4]]
print(f) # [[1, 2]]

print(f[0][0]) #1
f[0][0]=2
print(e) # [[1, 2], [3, 4]]
print(f) # [[2, 2]]
