l = [1, 2, 3, 4, 5, -1, -2, 4, 5]


def add_two_nums(l):
    l1 = set(l)
    print(l1)
    for i in l:
        if -i in l1:
            return True
    return False


l = [1, 2, 3, 4, 5, -1, -2, 4, 5]
# l = [1, 2, 3, 4]
print(add_two_nums(l))
