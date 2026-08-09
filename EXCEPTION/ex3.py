try:
    num=int(input("Enter the number:"))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Everything executed successfully.")