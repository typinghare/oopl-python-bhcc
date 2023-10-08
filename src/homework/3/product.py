"""Product module."""


class Product:
    """Vending machine product."""

    def __init__(self, name: str):
        """
        Creates a product.
        :param name: The name of the product.
        """
        self.product_name: str = name

    def consume(self):
        """Consumes this product."""
        print("Sorry, this product is empty.")


class Drink(Product):
    """Drink product."""

    def consume(self):
        print(f"Yum, you drink the {self.product_name}.")


class Snack(Product):
    """Snack product."""

    def consume(self):
        print(f"Yum, you eat the {self.product_name}.")
