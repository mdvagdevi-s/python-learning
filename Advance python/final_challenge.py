numbers = [1, 2, 3, 4, 5, 6]

a=filter(lambda x:x%2==0,numbers)

b=map(lambda x:x*x,a)

print(list(b))