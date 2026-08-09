try:
    num=int(input("Enter the number:"))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a valid number")

finally:
    print("Everything executed successfully.")