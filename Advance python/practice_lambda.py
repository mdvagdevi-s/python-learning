
#Create a lambda function called square that takes a number and returns its square.
square=lambda x:x*x
print(square(6))


#Create a lambda function called add that takes two numbers and returns their sum.
add=lambda a,b:a+b
print(add(10,20))


#Create a lambda function called check that:
#returns "Positive" if the number is greater than 0
#returns "Not Positive" otherwise

check=lambda x:"Positive" if x>0 else "Not positive"
print(check(5))
print(check(-2))
print(check(0))