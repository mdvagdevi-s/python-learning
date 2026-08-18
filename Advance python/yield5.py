def multipleof3():
    for i in range(1,6):
        yield i*3

m=multipleof3()
#print(next(m))
#print(next(m))
#print(next(m))
#print(next(m))
#print(next(m)) instead of using like this to get result we can use for loop

for value in m:
    print(value)