# Task: Ticket Price Calculator

from ticket import get_category, get_price



def main():
    name = input("Your name: ")
    age = int(input("Your age: "))
    is_student = input("Are you a student? (yes/no): ").lower() == "yes"


    category = get_category(age)
    price = get_price(category, is_student)

    print(f"{name.upper()} ({category.upper()}) pays GHS {price:.2f}")
    print(name.upper())
    print(f"Your name has {len(name)} letters")
    

if __name__ == "__main__":
    main()