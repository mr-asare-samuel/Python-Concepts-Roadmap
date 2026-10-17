def ask_age() -> int:
    """Ask for an age until the user types a whole number from 0 to 120."""
    while True:
        try:
            age = int(input("Age: "))
        except ValueError:
            print("Enter a valid age")
            continue

        if 0 <= age <= 120:
            return age
        print("Enter age from 0 to 120")



age = ask_age()
print(f"Your age is {age}")