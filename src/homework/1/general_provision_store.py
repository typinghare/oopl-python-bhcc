from typing import List

# [Environment]
# Python 3.11.4
# macOS 13.4.2_1

# All goods for sale in the store. I used a dict to represent the goods, but it messed up their
# orders; It turns out that using list and tuple is a nice approach in this case.
goods: List[tuple[str, int]] = [
    ("Food rations", 6),
    ("Water Flask", 3),
    ("Dagger", 12),
    ("Helmet", 32),
]


def general_provision_store():
    """Welcome to my General Provision Store game. Here you will play a customer and order items,
    and I will sum them up and give you a receipt.
    """

    print("Welcome to the General Provisions Store!")

    # A list of choices (indices of goods)
    choices: List[int] = []

    # Apply an infinite loop to simulate an order scenario
    while True:
        print("What can I get you today?")
        print_goods()

        # Prompt the user to input a choice
        choice = input("Enter 0-3 or q to end> ")

        # Break the order loop if the input is 'q'
        if choice.lower() == "q":
            print("\nOk, here is your receipt.")
            break

        num_choice = int(choice)
        if 0 <= num_choice < 4:
            choices.append(num_choice)
            print(f"\nGot it. You selected {goods[num_choice][0]}.")
        else:
            print(f"\nIllegal choice given: [ {choice} ].")

    # Print receipt; calculate the total in the iteration
    total = 0
    for choice in choices:
        name, price = goods[choice]
        print(f"{name}: {price} gold pieces.")
        total += price
    print(f"Today's Total is {total} gold pieces.")


def print_goods():
    """Prints all goods on the console."""
    for index, (name, price) in enumerate(goods):
        print(f"{index}. {name}: {price} gold pieces.")


# Start the game
general_provision_store()
