f=open("abc.txt","r")
data=f.read()
data=data.lower()
if "hi" in data:
    print("Yes LIve word is present in the file")
else:
    print("NO")