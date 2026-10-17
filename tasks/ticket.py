BASE_PRICE = 50

def get_category(age):
    if age < 13:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"

    
def get_price(category, is_student):
    if category == "Child":
        price = BASE_PRICE * 0.5
    elif category == "Teen":
        price = BASE_PRICE * 0.8
    elif category == "Adult":
        price = BASE_PRICE
    else:
        price = BASE_PRICE * 0.6

    if is_student and category != "Child":
        price = price - 10

    return price


if __name__ == "__main__":
    print("ticket.py was run directly")