def square():
    for i in range(1,6):
        yield i*i

s=square()

print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
