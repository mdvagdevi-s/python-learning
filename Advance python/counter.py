from collections import Counter
numbers=[1,2,2,3,3,3]
res=Counter(numbers)
print(res)

numbers = [1, 2, 2, 3, 3, 3, 4, 4]
count = Counter(numbers)
print(count.most_common())
print(count.most_common(1))