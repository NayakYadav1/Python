def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    age = int(input("Enter your age: "))
    validate_age(age)
except ValueError as e:
    print(e)