def outer(n):
    def inner(x):

        x*=n
        return x
    return inner
multiply_by_10=outer(10)

print(multiply_by_10(5))
print(multiply_by_10(7))