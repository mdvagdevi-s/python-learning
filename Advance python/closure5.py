def outer(n):
    def inner(x):

        x+=n
        return x
    return inner
add5=outer(5)

print(add5(10))
print(add5(20))