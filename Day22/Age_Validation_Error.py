def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
try:
    validate_age(-5)
except ValueError as e:
    print(f"ValueError: {e}")