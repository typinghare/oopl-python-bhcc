# from typing import List
#
#
# # [Environment]
# # Python 3.11.4
# # macOS 13.4.2_1
#
# # [About Black Citadel]
# # In the land of whimsy and wonder, there stands the Black Citadel, and old, spooky citadel haunted with ghosts. These
# # wandering spirits were once brave soldiers who fought in an intense war a long time ago. Legend has it that somewhere
# # inside the citadel, there is an awesome treasure map to be discovered! Loads of daring adventurers have come to the
# # Black Citadel, all excited to find the treasure map. However, nobody has ever made it out of there!
# #
# # The structure of the Black Citadel is simple. It can be divided in 10 blocks:
# # ===============
# # || 7 | 8 | 9 ||   ==> 3rd floor
# # || 4 | 5 | 6 ||   ==> 2nd floor
# # || 2_1 | 2 | 3 ||   ==> 1st floor
# # ===============
# #      | 0 |
# #
# # Now, you (the player) is standing at the entrance of the Black Citadel (position 0).
#
#
# class Action:
#     """Enumeration of actions the player can apply."""
#
#     UP = 0  # Go upstairs
#     RIGHT = 1  # Go rightwards
#     DOWN = 2  # Go downstairs
#     LEFT = 3  # Go leftwards
#     LOOK = 4  # Look around
#     INVESTIGATE = 5  # Investigate the room
#     ENTER = 6  # Enters the Black Citadel
#     OUT = 7  # Get out of the Black Citadel
#
#
# def bold(string: str) -> str:
#     """Wrap a string in ANSI escape codes to make it bold and blue when printed on the terminal.
#     :param string: The string to format.
#     :return: The formatted string.
#     """
#     return f"\033[1;36m{string}\033[0m"
#
#
# # Game resources
# resources = {
#     # The actions the player can choose in each block
#     "actions": [
#         [Action.LOOK, Action.ENTER],
#         [Action.LOOK, Action.INVESTIGATE, Action.UP, Action.RIGHT],
#         [
#             Action.LOOK,
#             Action.INVESTIGATE,
#             Action.UP,
#             Action.LEFT,
#             Action.RIGHT,
#             Action.OUT,
#         ],
#         [Action.LOOK, Action.INVESTIGATE, Action.UP, Action.LEFT],
#         [Action.LOOK, Action.INVESTIGATE, Action.UP, Action.DOWN, Action.RIGHT],
#         [
#             Action.LOOK,
#             Action.INVESTIGATE,
#             Action.UP,
#             Action.DOWN,
#             Action.LEFT,
#             Action.RIGHT,
#         ],
#         [Action.LOOK, Action.INVESTIGATE, Action.UP, Action.DOWN, Action.LEFT],
#         [Action.LOOK, Action.INVESTIGATE, Action.DOWN, Action.RIGHT],
#         [Action.LOOK, Action.INVESTIGATE, Action.DOWN, Action.LEFT, Action.RIGHT],
#         [Action.LOOK, Action.INVESTIGATE, Action.DOWN, Action.LEFT],
#     ],
#     # The names of blocks
#     "name": [
#         "entrance to the citadel",
#         "room 101",
#         "room 102",
#         "room 103",
#         "room 201",
#         "room 202",
#         "room 203",
#         "room 301",
#         "room 302",
#         "room 303",
#     ],
#     # Mapping from word (lowercase) to action
#     "word_action_dict": {
#         "up": Action.UP,
#         "right": Action.RIGHT,
#         "down": Action.DOWN,
#         "left": Action.LEFT,
#         "look": Action.LOOK,
#         "investigate": Action.INVESTIGATE,
#         "enter": Action.ENTER,
#         "out": Action.OUT,
#     },
#     # The prompt strings to be printed to the terminal
#     "action_prompt": [
#         f'go {bold("up")}stairs',
#         f'go to the {bold("right")} room',
#         f'go {bold("down")}stairs',
#         f'go to the {bold("left")} room',
#         f'{bold("look")} around',
#         f'{bold("investigate")} the room',
#         f'{bold("enter")} the Black Citadel',
#         f'get {bold("out")} of the Black Citadel',
#     ],
#     "text": {
#         Action.LOOK: [
#             "The Black Citadel sits atop a misty hill, surrounded by a mysterious forest that whispers secrets to the "
#             "rustling leaves and curious critters.",
#             "This room is for servants. You feel a uneasy staring at your back...",
#             "This is the hall of the citadel. There is a grand staircase leading to the second floor.",
#             "This room is messy and full of cabinets. Guess it was a larder.",
#             "There is a big table in the room. It looks like a dining room.",
#             "There are a lot of paintings in this room. Some of the paintings fell on the ground.",
#             "This room looks like a bedroom, but there is only a bed frame and a cabinet.",
#             "This room is very luxurious. It seems to be the sleeping quarter of the owner of this citadel.",
#             "This room is completely empty. You feel a cool breeze at your back...",
#             "There are many bookshelves and tomes in this room. Lots of documents are scattered on the floor.",
#         ],
#         Action.INVESTIGATE: [
#             None,
#             "Nothing here.",
#             "Nothing here.",
#             "There is a rotten apple on the ground. But why it has not been completely decomposed?",
#             "There is a sparkling fork on the table.",
#             "You found a piece of old paper behind a painting frame. It is part of the treasure map!",
#             "Nothing here.",
#             "Nothing here.",
#             "Nothing here.",
#             "You found a piece of old paper. It is part of the treasure map!",
#         ],
#         Action.ENTER: ["You entered the Black Citadel. Good luck!"],
#     },
#     # These blocks contain the pieces of the treasure map
#     "treasure_map_block": [5, 9],
# }
#
#
# def text_based_adventure_game():
#     print_backstory()
#     print(
#         "Now you are standing at the entrance of the Black Citadel. You can either enter the Black Citadel or turn "
#         "back."
#     )
#
#     position = 0  # the position of the player
#     has_entered = False  # whether the player has entered the citadel
#     treasure_map_piece_num = 0  # the number of treasure map pieces
#     investigated = [False] * 10  # whether a block has been investigated
#     while True:
#         name = resources["name"][position]
#         actions = resources["actions"][position]
#
#         # Print the prompt
#         print(f"\nYou are at the {name}.")
#         print(f"You can {actions_to_prompt(actions)}.")
#         if treasure_map_piece_num == 2:
#             print("Something is chasing you. You should leave the citadel ASAP.")
#
#         # Let player input an action word
#         action_word = input("What will you do > ").lower()
#
#         # Check if the action word is valid
#         if action_word not in resources["word_action_dict"]:
#             print(f"Invalid action: {bold(action_word)}")
#             continue
#
#         # Get the corresponding action (int)
#         action = resources["word_action_dict"][action_word]
#
#         # Check if the action is valid
#         if action not in actions:
#             print(f"Invalid action: {bold(action_word)}")
#             continue
#
#         # Print the text
#         print_text(action, position, investigated)
#
#         # If the action is Action.INVESTIGATE, check if the block contain the pieces of treasure map
#         if action == Action.INVESTIGATE and not investigated[position]:
#             if position in resources["treasure_map_block"]:
#                 treasure_map_piece_num += 1
#                 print("You put the piece of treasure map in your pocket.")
#             investigated[position] = True
#
#             # If two pieces of treasure map are gathered
#             if treasure_map_piece_num == 2:
#                 print("You have gathered all pieces of treasure map. ESCAPE!!!")
#
#         # Change the current position
#         position = change_position(position, action)
#         if position > 0:
#             has_entered = True
#
#         # If the position is 0, which is at the entrance of the citadel, and the player has entered the citadel,
#         # the game is over.
#         if has_entered and position == 0:
#             game_over(treasure_map_piece_num)
#
#
# def print_backstory():
#     """Print the backstory of this game."""
#     backstory = (
#         "In the land of whimsy and wonder, there stands the Black Citadel, and old, spooky citadel haunted"
#         "ghost. These wandering spirits were once brave soldiers who fought in an intense war a long time ago"
#         ". Legend has it that somewhere inside the citadel, there is an awesome treasure map to be discovered"
#         "! Loads of daring adventurers have come to Black Citadel, all excited to find the treasure map."
#         "However, nobody has ever made it out of there!"
#     )
#
#     print("\n".join(backstory))
#
#
# def actions_to_prompt(actions: List[int]) -> str:
#     """Converts actions (list) into a prompt string.
#     :return: A prompt string.
#     """
#     prompts = [resources["action_prompt"][action] for action in actions]
#
#     if len(prompts) > 1:
#         prompts[-1] = "or " + prompts[-1]
#
#     return ", ".join(prompts)
#
#
# def print_text(action: int, position: int, investigated: List[bool]):
#     """Prints text after selecting an action.
#     :param action: The action selected.
#     :param position: The current position.
#     :param investigated: The investigated list.
#     """
#     if action == Action.INVESTIGATE and investigated[position]:
#         print("You have investigated this room.")
#
#         return
#
#     if action in resources["text"]:
#         text_list = resources["text"][action]
#         if len(text_list) > position and text_list[position] is not None:
#             print(text_list[position])
#     else:
#         # Go to another place
#         print("......")
#
#
# def change_position(position: int, action: int) -> int:
#     """Changes the position based on a specific action.
#     :param position: The original position.
#     :param action: The action to take. Should be one of the Action enum values.
#     :return: The new position after applying the action.
#     """
#     if action == Action.UP:
#         return position + 3
#     if action == Action.RIGHT:
#         return position + 1
#     if action == Action.DOWN:
#         return position - 3
#     if action == Action.LEFT:
#         return position - 1
#     if action == Action.ENTER:
#         return 2
#     if action == Action.OUT:
#         return 0
#
#     # Action.LOOK and Action.INVESTIGATE does not affect the position, returns the original position
#     return position
#
#
# def game_over(treasure_map_piece_num: int):
#     """Game over process.
#     :param treasure_map_piece_num: The number of treasure map pieces the player gathered
#     """
#     if treasure_map_piece_num == 0:
#         print("\nGame over. You haven't found the treasure map ...")
#     elif treasure_map_piece_num == 1:
#         print("\nGame over. You haven't found all pieces of the treasure map ...")
#     elif treasure_map_piece_num == 2:
#         print(
#             "\nGame over. You've found the treasure map. It's time to embark on a new journey."
#         )
#
#     # Print author's information
#     print("\n" + "=" * 80 + "\n")
#     print("Game name: The Black Citadel")
#     print("Author: James Chan")
#     print("Creation date: Sep 14, 2023")
#     print(
#         "Special Thanks: ChatGPT helped me refine the backstory and room descriptions."
#     )
#
#     exit(0)
#
#
# # Start the game
# text_based_adventure_game()
