"""Box module."""


class Box:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} {self.quantity}"