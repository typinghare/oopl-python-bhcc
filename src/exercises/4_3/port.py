"""Port module"""


class Port:
    def __init__(self, name, max_depth):
        self.name = name
        self.max_depth = max_depth
        self.ships_in_port = []

    def __repr__(self):
        return f"name: {self.name} max_depth:{self.max_depth}"
