def count_of_char(s):
    count = 0
    for i in s:
        if i == 'l':
            count = count + 1
    return count


s = 'Hello'
res = count_of_char(s)
print(res)


