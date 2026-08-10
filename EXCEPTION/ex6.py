try:
    age = int(input("Enter age: "))

    if age < 18:
        raise ValueError("Not Eligible")

    print("Eligible")

except ValueError as e:
    print(e)

    #e=ValueError("Not Eligible")  it will print the sentence inside