"""Blocks."""
from typing import List
import action

Action = action.Action

# Names of blocks
names: List[str] = [
    "the entrance",
    "the servants' bedroom (101)",
    "the hall",
    "the larder (103)",
    "the dining room (201)",
    "the exhibition room (202)",
    "the unknown room (203)",
    "the master bedroom (301)",
    "the utility room (302)",
    "the library (303)",
    "the secret room",
]

# Descriptions of blocks
descriptions: List[str] = [
    "A giant door stands in front of you.",
    "There are several beds and nightstands in this room.",
    "There is a grand staircase leading to the second floor.",
    "There are many cockroaches and rats here.",
    "There is a big table in the center of the room.",
    "There are lots of paintings in this room. Some of them are on the ground.",
    "This room looks like a bedroom, but there is only a bed frame and a cabinet.",
    "This room is very luxurious.",
    "This room is quite empty. You feel a cool breeze at your back...",
    "There are many bookshelves and tomes in this room. Lots of documents are scattered on the "
    "floor.",
    "This room is pretty small. There are two bookshelves here.",
]

# These blocks contain the pieces of the treasure map
treasure_maps: List[int] = [5, 10]

# Lambda functions for changing position
lambda_mapping = {
    Action.UP: lambda pos: pos + 3,
    Action.RIGHT: lambda pos: pos + 1,
    Action.DOWN: lambda pos: pos - 3,
    Action.LEFT: lambda pos: pos - 1,
    Action.ENTER: lambda pos: 2 if pos == 0 else 10,
    Action.LEAVE: lambda pos: 0 if pos == 2 else 9,
}


def change_position(position: int, player_action: int):
    """Applies an action on the position, and returns the new position
    :param position The index of the block where the player current is
    :param player_action The action to apply
    :return: The new position after applying the action.
    """

    # Other actions do not change the position
    new_position = lambda_mapping.get(player_action, lambda pos: pos)(position)

    if new_position != position:
        print("......")

    return new_position
