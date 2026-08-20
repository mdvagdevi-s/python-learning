def multiply(*num):
    res=1

    for n in num:
        res*=n

    return res

print(multiply(2,4,6))