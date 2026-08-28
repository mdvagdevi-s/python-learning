import re
text="apple banana mango orange"
result=re.findall(r"[ab]",text)
print(result)

a="Python 123 AI 456"
res=re.findall(r"[0-9]+",a)
print(res)

text = "Python 123 AI"
result = re.findall(r"\w+", text)
print(result)

b = "My PIN is 1234"
result = re.findall(r"\d{4}", b)
print(result)


c="I love Java"
r=re.sub(r"Java","Python",c)
print(r)


d = "I have 3 cats and 2 dogs"
s= re.sub(r"\d+", "many", d)
print(s)


e = "Hello Vagdevi"
t = re.search(r"^Hello", e)
print(t.group())
#^ → beginning
#$ → end

f = "My marks are 85"
u= re.search(r"(\d)(\d)", f)
print(u.group())
print(u.group(1))
print(u.group(2))

g="I Like Python"
v=re.search(r"Python|Java",g)
print(v.group())

h="Hello 123!"
w=re.findall(r"[^a-zA-Z]",h)
print(w)

i="Contact me at vags@gmail.com"
x=re.findall(r"\w+@\w+\.\w+",i)
print(x)


j= "Emails: abc@gmail.com, xyz123@yahoo.com"
y = re.findall(r"\w+@\w+\.\w+", j)
print(y)

k= "Python,DSA;SQL|AI"
z = re.split(r"[,;|]", k)
print(z)