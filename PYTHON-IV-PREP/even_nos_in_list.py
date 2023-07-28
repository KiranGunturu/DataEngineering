l1 = [2, 1, 3, 7, 12, 17]


def even_nos(l1):
    for i in l1:
        if i % 2 == 0:
            print(i)


# even_nos(l1)

def even_nos(l1):
    even_numbers = []
    for i in l1:
        if i % 2 == 0:
            even_numbers.append(i)
    #return even_numbers
    print(even_numbers)


l1 = [2, 1, 3, 7, 12, 17]
#res = even_nos(l1)
#print(res)
even_nos(l1)



def evennumbs():
    x = int(input("enter number"))
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

# evennumbs()
