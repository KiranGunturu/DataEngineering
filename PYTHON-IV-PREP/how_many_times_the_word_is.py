def count_no_of_chars(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


# s = ['Hello', 'Kiran', 'Hello']
s = "hello"
res = count_no_of_chars(s)
print(res)

# {'Hello': 2, 'Kiran': 1}
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
