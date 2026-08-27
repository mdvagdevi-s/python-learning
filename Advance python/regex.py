import re
text="apple banana mango orange"

result=re.findall(r"[ab]",text)
print(result)