class AgeError(Exception):
    pass

age=int(input("Enter Age:"))

if age<15:
    raise AgeError("You are not eligible to vote")

print("Eligible")