# string1=input("Enter you first string:")
# #string2=input("enter your second string to be checked:")
#
# resString=string1[::-1]
# print(resString)
#
# if string1 == resString:
#     print("entered string is a palindorme")
# else:
#     print("Not a palindrome")

# --------------
# def ispalindrome(string):
#     return string == string[::-1]
#
# string="hello"
# res=ispalindrome(string)
#
# if res:
#     print("yes")
# else:
#     print("No")

def ispal(s):
    res= ''.join(reversed(s))

    if s == res:
        return True
    return False

s="malayalam"
ans=ispal(s)

if ans:
    print("True")
else:
    print("False")
