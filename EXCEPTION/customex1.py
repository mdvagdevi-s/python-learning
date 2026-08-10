class NegativeNumberError(Exception):
    pass
try:
    num=int(input("Enter number:"))
    if num<0:
        raise NegativeNumberError("Negative numbers are not allowed")

    print("Valid number")
except NegativeNumberError as e :
    print(e)