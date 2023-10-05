"""Container module"""


class Container:
    def __init__(self):
        self.box_list = []

    def __repr__(self):
        return f"boxes: {self.box_list}"
