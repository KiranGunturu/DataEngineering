str = 'madam'
def isPal(str):
    return str == str[::-1]

res = isPal(str)
print(res)

####################

str = 'madam'
rev_str = ''
for chr in str:
    rev_str = chr+rev_str
if(str==rev_str):
    print(str, "is palindrome")
else:
    print(str, "is not a palindrome")


