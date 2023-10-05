"""Ship module"""


class Ship:
    def __init__(self, name, country, num_container):
        self.name = name
        self.country = country
        self.num_container = num_container
        self.container_list = []

    def __repr__(self):
        return (
            f"name: {self.name}, country: {self.country}, "
            f"max number of containers: {self.num_container}, "
            f"container list: {self.container_list}"
        )
