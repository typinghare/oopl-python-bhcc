"""Vending module."""
from typing import List, Dict
from product import Product


class VendingMachine:
    """Vending machine."""

    def __init__(self):
        self._slots: Dict[str, Slot] = {}
        self.total_sales = 0

    def stock_item(
        self, slot_name: str, product_list: List[Product], unit_price: float
    ):
        """
        Stocks items to a specified slot.
        :param slot_name: The name of the slot.
        :param product_list: List of products to store.
        :param unit_price: The unit price of the product.
        :return:
        """
        self._slots[slot_name] = Slot(product_list, unit_price)

    def print_inventory(self):
        """Prints all slots."""
        print("-" * 35)

        for slot_name, slot in self._slots.items():
            print(slot_name)
            for product in slot.product_list:
                print(f"- {product.product_name}")

        print("-" * 35)

    def purchase(self, slot_name: str, money_input: float) -> (Product, float):
        """
        Purchases a product from a specified slot.
        :param slot_name: The name of the slot.
        :param money_input: The money the customer put into the vending machine.
        :return: The product if the money is enough.
        """

        # Get the slot
        slot = self._slots.get(slot_name)

        # Check if the slot exists
        if slot is None:
            return Product("Empty Product"), money_input

        # Check if money is enough
        unit_price = slot.get_unit_price()
        if unit_price > money_input:
            return Product("Empty Product"), money_input

        # Dispense product
        product = slot.remove_product()
        self.total_sales += unit_price
        return product, money_input - unit_price


class Slot:
    """Vending machine slot."""

    def __init__(
        self,
        product_list: List[Product],
        unit_price: float,
    ):
        self.product_list = product_list
        self._unit_price = unit_price

    def remove_product(self) -> Product:
        """Removes a product from this slot."""
        return self.product_list.pop()

    def get_unit_price(self) -> float:
        """Returns the unit price of products in this slot."""
        return self._unit_price
