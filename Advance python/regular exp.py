import re

text =  "I bought 10 apples, 5 oranges and 20 bananas"

result = re.findall(r"\d+", text)

print(result)