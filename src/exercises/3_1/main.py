some_books = [
    {"author": "", "title": "", "price": 25.9},
    {"author": "", "title": "", "price": 49.9},
]


def calculate_total(books):
    """Calculates the total price of the books."""
    # price = 0
    # for book in books:
    #     price += book["price"]
    #
    # return price
    return sum(book["price"] for book in books)


def calculate_shipping(total_price):
    """Calculates the shipping price."""
    return 0 if total_price > 100 else 3.99


def checkout(books):
    answer = input("Do you want to checkout? (yes/no)")
    if answer.lower() == "no":
        print("Come back soon!")
        return

    total_price = calculate_total(books)
    shipping_price = calculate_shipping(total_price) + total_price
    print(f"Total price     ${total_price}")
    print(f"Shipping price  ${round(shipping_price,2)}")
    print(f"Final price     ${round(total_price + shipping_price,2)}")


checkout(some_books)
