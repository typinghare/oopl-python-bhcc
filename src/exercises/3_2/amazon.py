def calculate_total(books):
    """Calculates the total price of the books."""
    return sum(book["price"] for book in books)


def calculate_shipping(total_price):
    """Calculates the shipping price."""
    return 0 if total_price > 100 else 3.99


def checkout(books):
    """Checkout."""
    answer = input("Do you want to checkout? (yes/no)")
    if answer.lower() == "no":
        print("Come back soon!")
    elif answer.lower() == "yes":
        total_price = calculate_total(books)
        shipping_price = calculate_shipping(total_price)
        print(f"Total price     ${format(total_price, '.2f')}")
        print(f"Shipping price  ${format(shipping_price, '.2f')}")
        print(f"Final price     ${format(total_price + shipping_price, '.2f')}")
    else:
        print("I am sorry?")
