def count_down():
    for i in range(5,0,-1):
        yield i

c=count_down()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
