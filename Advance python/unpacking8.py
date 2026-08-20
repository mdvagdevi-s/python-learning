a = {"name": "Vagdevi"}
b = {"age": 20}

result = {**a, **b}
print(result)

student = {"name": "Vagdevi", "age": 20}
course = {"course": "AI", "year": 3}
aa={**student,**course}
print(aa)



a = [1, 2,3]
b = [4,5,6]

result = [*a, *b]
print(result)