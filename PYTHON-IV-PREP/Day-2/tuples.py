# tuples
# tuples are immutable
a = (1, 2, 3)
print(type(a))
print(a[0])  # 1
a = ('CSK', 'MI')  # it will not overwrite the above a
print(type(a))
b = list(a)  # convert tuple to a list

# dict
# mutable

ipl = {
    "CSK": "Chennai Super Kings",
    "MI": "Mumbai Indians"
}
print(ipl)
print(type(ipl))
print(ipl["CSK"])
print(ipl["MI"])
ipl["GT"] = "Gujarat Titans"  # add to the existing list
ipl["CSK"] = "Chennai"  # overwrite the existing key value
print(ipl)
del ipl["CSK"]  # delete the key and value

# nested dict
ipl = {
    "CSK" : {"Name":"Chennai Super Kings","Captain": "MSD"},
    "MI": {"Name": "Mumbai Indians","captain":"Rohit"},
    "RCB": {"Name": "Royal Challenges Bangalore"}
}

print(ipl)


# boolean

1==1
print(type(1==1))