class Building:
    def __init__(self, name):
        """
        Creates a building.
        :param name: The name of this building.
        """
        self.name = name
        self._rooms = []

    def add_room(self, room_number):
        """
        Adds a room to this building.
        :param room_number: The number of this room.
        :return: The room created.
        """
        room = Room(room_number, self)
        self._rooms.append(room)

        return room

    def get_number_rooms(self):
        """Returns the number of rooms in this building."""
        return len(self._rooms)


class Room:
    def __init__(self, number, building):
        """
        Creates a room.
        :param number: The number of this room.
        :param building: The building where this room locates.
        """
        self.number = number
        self.building = building


building0 = Building("Empire State Building")
building0.add_room("251")
building0.add_room("252")
print(f"Number of rooms in building:  {building0.get_number_rooms()}")
