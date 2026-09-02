students = [
    ("Vagdevi", "CSE"),
    ("Shilpa", "ISE"),
    ("Rahul", "CSE")
]
from collections import defaultdict

res=defaultdict(list)
for name,branch in students:
    res[branch].append(name)

print(res)



count = defaultdict(int)
count["Python"] += 1
count["Python"] += 1
count["DSA"] += 1
print(count)