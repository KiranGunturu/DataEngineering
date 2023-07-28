l = [0, 1, 2, 3, 4, 5, 7, 8, 9]  # 6


# l = [0, 1, 6,2,5,4] #3


def missing_nums(l):
    list_dict = {}
    for i in l:
        list_dict[i] = True

    # output of list_dict
    # 0:True
    # 1:True
    # 2:True
    # 3:True
    # 4:True
    # 5:True
    # 7:True
    # 8:True
    # 9:True
    for i in range(len(l) + 1):
        #print(i, list_dict.get(i))
        if not list_dict.get(i):
            return i
    return None


print(missing_nums(l))
