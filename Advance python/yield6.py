def even_sq():
    for i in range(1,11):
        if i%2==0:
            yield i*i

e=even_sq()

for v in e:
    print(v)