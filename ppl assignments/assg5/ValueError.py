try:
    age = int(input("Enter age: "))
    if age < 18:
        raise ValueError;
    else:
        print("Valid Age")
except ValueError:
    print("Invalid age")