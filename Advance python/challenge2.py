from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]

a=filter(lambda x:x%2==0,numbers)

b=map(lambda x:x*x,a)

c=reduce(lambda p,q:p+q,b)

print(c)