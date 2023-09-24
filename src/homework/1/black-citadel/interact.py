"""Interactions."""
from typing import Tuple

import action

Action = action.Action

word_action_mapping = {
    "up": Action.UP,
    "upstairs": Action.UP,
    "down": Action.DOWN,
    "downstairs": Action.DOWN,
    "right": Action.RIGHT,
    "left": Action.LEFT,
    "look": Action.LOOK,
    "investigate": Action.INVESTIGATE,
    "enter": Action.ENTER,
    "leave": Action.LEAVE,
}


def input_action() -> Tuple[int, str]:
    """Prompts the user to enter an action string, and parses the input into an action
    :return a tuple contains an action and the original action string; `Action.INVALID` is returned
    if the action string is not valid
    """
    action_str = input("What will you do> ").lower()
    words = action_str.split(" ")

    for word in words:
        if word in word_action_mapping:
            return word_action_mapping[word], action_str

    return Action.INVALID, action_str
