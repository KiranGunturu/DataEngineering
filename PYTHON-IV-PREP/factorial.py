def factori(n):
    if n == 0:
        return 1
    else:
        return n * factori(n - 1)


print(factori(5))


# using for loop

n = 5
result = 1
for i in range(n, 0, -1):
    result = result * i

print(result)