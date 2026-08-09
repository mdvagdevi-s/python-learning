try:
    num1=int(input("Enter NUM1:"))
    num2=int(input("Enter NUM2:"))
    print(num1/num2)

except ZeroDivisionError:
    print("Cannot divide by zero")