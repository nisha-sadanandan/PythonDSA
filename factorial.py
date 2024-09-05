def fact(n):
    f = 1

    for i in range(1,n):
        f = f * i

    return f
x = 5
result = fact(5)
print(result)
