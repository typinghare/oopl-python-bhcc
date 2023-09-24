"""Actions enum and actions of blocks."""
from typing import List
import utils


class Action:
    """Actions enum."""

    INVALID = -1  # Invalid action
    UP = 0  # Go upstairs
    DOWN = 1  # Go downstairs
    LEFT = 2  # Go leftwards
    RIGHT = 3  # Go rightwards
    LOOK = 4  # Look around
    INVESTIGATE = 5  # Investigate a room
    ENTER = 6  # Enter Black Citadel
    LEAVE = 7  # Leave Black Citadel


# Available actions for each block
available: List[List[int]] = [
    [Action.LOOK, Action.ENTER],
    [Action.LOOK, Action.INVESTIGATE, Action.RIGHT],
    [
        Action.LOOK,
        Action.INVESTIGATE,
        Action.UP,
        Action.LEFT,
        Action.RIGHT,
        Action.LEAVE,
    ],
    [Action.LOOK, Action.INVESTIGATE, Action.LEFT],
    [Action.LOOK, Action.INVESTIGATE, Action.UP, Action.RIGHT],
    [
        Action.LOOK,
        Action.INVESTIGATE,
        Action.UP,
        Action.DOWN,
        Action.LEFT,
        Action.RIGHT,
    ],
    [Action.LOOK, Action.INVESTIGATE, Action.UP, Action.DOWN, Action.LEFT],
    [Action.LOOK, Action.INVESTIGATE, Action.RIGHT],
    [Action.LOOK, Action.INVESTIGATE, Action.DOWN, Action.LEFT, Action.RIGHT],
    [Action.LOOK, Action.INVESTIGATE, Action.DOWN, Action.LEFT, Action.ENTER],
    [Action.LOOK, Action.INVESTIGATE, Action.LEAVE],
]

# Action scripts
scripts = {
    Action.LOOK: [
        "The Black Citadel sits atop a misty hill, surrounded by a mysterious forest that whispers "
        "secrets to the rustling leaves and curious critters.",
        "There are some tattered clothes on the ground. You feel an disturbing starting at your "
        "back...",
        "It is so empty. You can clearly hear the echo of your footsteps.",
        "This room is messy and full of cabinets. Some glass jars are in the cabinets.",
        "Nothing special in this room. Perhaps it is not worth investigating.",
        "The biggest painting in this room is the portray of a king. Outside of the room, there "
        "are two stairs in both sides.",
        "There are strange words written on the wardrobe. The wardrobe makes a squeaky sound from "
        "time to time.",
        "There are a wardrobes and cabinets in this room. However, they are open and most of "
        "them are empty.",
        "There is a big sack in the corner. You feel an ominous breeze at your back...",
        "There seems to be a secret room in the end of the room. Do you want to enter it?",
        "All books are all covered in a thick layer of dust. You can't see their names unless you "
        "wipe off the dust.",
    ],
    Action.INVESTIGATE: [
        "",
        "Nothing here.",
        "Nothing here.",
        "There is a rotten apple on the ground. But why hasn't it been completely decomposed?",
        "There is a sparkling fork on the table.",
        "You find a piece of old paper behind a painting frame. It is part of the treasure map!",
        "Nothing here.",
        "Nothing here.",
        "Nothing here.",
        "You find an old tome, inside which there is a rusted key.",
        "You find a piece of old paper in an old tome. It is part of the treasure map!",
    ],
    Action.ENTER: [
        "You entered the Black Citadel. Here is how the game is played: \n"
        f"Type to go {utils.bold('up')}stairs, {utils.bold('down')}stairs, {utils.bold('left')}, "
        f"and {utils.bold('right')}. You can also {utils.bold('look')} around the room and "
        f"{utils.bold('investigate')} the room. However, you only have SIX chances to investigate "
        f"since investigations will take up much time. You can {utils.bold('leave')} the citadel "
        f"from the hall.",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "You entered a hidden room.",
    ],
}

max_investigation = 6


def get_script(player_action: int, position: int) -> str:
    """Returns the script
    :param player_action The action the player chooses
    :param position The index of the position where the player is
    :return The script; empty string if no script is available
    """
    if player_action not in scripts or position >= len(scripts[player_action]):
        return ""

    return scripts[player_action][position]
