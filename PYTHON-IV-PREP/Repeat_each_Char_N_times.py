# iteration

s = 'Hello'
s1 = ''
for i in s:
    s1 = s1 + i * 3
print(s1)

# recursion

s = 'Hello'


def repeat_chars(s, n):
    if len(s) == 0:
        return ''
    return s[0] * n+repeat_chars(s[1:],n)


print(repeat_chars(s, 3))
