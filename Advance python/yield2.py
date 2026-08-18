def is_even():
    for i in range(1,11):
        if i%2==0:
            yield i

e=is_even()
print(next(e))

print(next(e))

print(next(e))

print(next(e))

print(next(e))