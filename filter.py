nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = list(filter(lambda n: n%2==0,nums))
print(even)

double = list(map(lambda n:n *2,nums))
print(double)

sum = reduce(lambda a,b: a+b ,nums)
print(sum)