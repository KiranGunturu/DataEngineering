def calc_bmi():
    weight = int(input("enter your age"))
    height = int(input("enter your height"))
    BMI = weight / (height ** height)
    return BMI


calc_bmi()

# replace all occurrences of a to b

name = "aaggniau"
print(type(name))
modified_str = ''
for chrs in range(0,len(name)):
    if name[chrs] == 'a' or name[chrs] == 'a'.upper():
        modified_str += 'b'
    else:
        modified_str += name[chrs]

print(modified_str)

# capitalize first letter
name = "STALLINGS is OUR CITY"
str = name.capitalize()
print(str)








