l = [1, 2, 3]


def count_list(l):
    if not l:
        return 0
    return 1 + count_list(l[1:])


# 1 1+[2,3]
# 2 1+1+[3]
# 3 1+1+1+[]
# 4 1+1+1+0

print(count_list(l))
