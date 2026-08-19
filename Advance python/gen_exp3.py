numbers = [1, 2, 3, 4, 5, 6]
even_sq=(x*x for x in numbers if x%2==0)

print(next(even_sq))
print(next(even_sq))
print(next(even_sq))
