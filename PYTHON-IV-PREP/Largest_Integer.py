l1 = [12, 14, 11, 67]


def maxInteger(l1):
    max = l1[0]
    print(max)
    for i in l1:
        if i > max:
            max = i
    return max


res = maxInteger(l1)
print(res)
