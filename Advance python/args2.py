def maximum(*numbers):
    large=numbers[0]

    for num in numbers:
        if num>large:
            large=num

    return large

print(maximum(10,20,30,40))