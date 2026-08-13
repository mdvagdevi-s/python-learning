numbers = [3, 7, 10, 12, 15, 18, 21, 24]

a=filter(lambda x:x>10,numbers)
b=map(lambda x:x*2,a)
print(list(b))