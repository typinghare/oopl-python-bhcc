# from typing import List
#
#
# # [Basic Info]
# # Name: The Black Citadel
# # Version: v1.1
# # Environment: Python 3.11.4; macOS 13.4.2_1
# # Changelog: (1) Apply 100 max columns; (2)
#
# # [About the Game]
# # In the land of whimsy and wonder, there stands the Black Citadel, and old, spooky citadel haunted
# # with ghosts. These wandering spirits were once brave soldiers who fought in an intense war a long
# # time ago. Legend has it that somewhere inside the citadel, there is an awesome treasure map to
# # Black Citadel, all excited to find the treasure map. However, nobody has ever made it out of
# # there!
# #
# # The structure of the Black Citadel is simple. It can be divided in 10 blocks:
# # ===============
# # || 7 | 8 | 9 ||   ==> 3rd floor
# # || 4 | 5 | 6 ||   ==> 2nd floor
# # || 1 | 2 | 3 ||   ==> 1st floor
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
# # The actions that the player can choose in each block
# game_actions: List[List[int]] = [
#     [Action.LOOK, Action.ENTER],
#     [Action.LOOK, Action.INVESTIGATE, Action.UP, Action.RIGHT],
#     [
#         Action.LOOK,
#         Action.INVESTIGATE,
#         Action.UP,
#         Action.LEFT,
#         Action.RIGHT,
#         Action.OUT,
#     ],
#     [Action.LOOK, Action.INVESTIGATE, Action.UP, Action.LEFT],
#     [Action.LOOK, Action.INVESTIGATE, Action.UP, Action.DOWN, Action.RIGHT],
#     [
#         Action.LOOK,
#         Action.INVESTIGATE,
#         Action.UP,
#         Action.DOWN,
#         Action.LEFT,
#         Action.RIGHT,
#     ],
#     [Action.LOOK, Action.INVESTIGATE, Action.UP, Action.DOWN, Action.LEFT],
#     [Action.LOOK, Action.INVESTIGATE, Action.DOWN, Action.RIGHT],
#     [Action.LOOK, Action.INVESTIGATE, Action.DOWN, Action.LEFT, Action.RIGHT],
#     [Action.LOOK, Action.INVESTIGATE, Action.DOWN, Action.LEFT],
# ]
#
# # The name of each block
# game_block_names: List[str] = [
#     "entrance to the citadel",
#     "room 101",
#     "room 102",
#     "room 103",
#     "room 201",
#     "room 202",
#     "room 203",
#     "room 301",
#     "room 302",
#     "room 303",
# ]
#
# # Mapping from a word (lowercase) to an action
# game_word_action_dict = {
#     "up": Action.UP,
#     "right": Action.RIGHT,
#     "down": Action.DOWN,
#     "left": Action.LEFT,
#     "look": Action.LOOK,
#     "investigate": Action.INVESTIGATE,
#     "enter": Action.ENTER,
#     "out": Action.OUT,
# }
#
# # The prompt strings to be printed to the terminal
# game_action_prompts: List[str] = [
#     f'go {bold("up")}stairs',
#     f'go to the {bold("right")} room',
#     f'go {bold("down")}stairs',
#     f'go to the {bold("left")} room',
#     f'{bold("look")} around',
#     f'{bold("investigate")} the room',
#     f'{bold("enter")} the Black Citadel',
#     f'get {bold("out")} of the Black Citadel',
# ]
#
# # The scripts in the game; when a player chooses an action in certain blocks, the corresponding
# # script shows up
# game_scripts = {
#     Action.LOOK: [
#         "The Black Citadel sits atop a misty hill, surrounded by a mysterious forest that whispers "
#         "secrets to the rustling leaves and curious critters.",
#         "This room is for servants. You feel a uneasy staring at your back...",
#         "This is the hall of the citadel. There is a grand staircase leading to the second floor.",
#         "This room is messy and full of cabinets. Guess it was a larder.",
#         "There is a big table in the room. It looks like a dining room.",
#         "There are a lot of paintings in this room. Some of the paintings fell on the ground.",
#         "This room looks like a bedroom, but there is only a bed frame and a cabinet.",
#         "This room is very luxurious. It seems to be the sleeping quarter of the owner of this "
#         "citadel.",
#         "This room is completely empty. You feel a cool breeze at your back...",
#         "There are many bookshelves and tomes in this room. Lots of documents are scattered on the"
#         " floor.",
#     ],
#     Action.INVESTIGATE: [
#         None,
#         "Nothing here.",
#         "Nothing here.",
#         "There is a rotten apple on the ground. But why hasn't it been completely decomposed?",
#         "There is a sparkling fork on the table.",
#         "You found a piece of old paper behind a painting frame. It is part of the treasure map!",
#         "Nothing here.",
#         "Nothing here.",
#         "Nothing here.",
#         "You found a piece of old paper. It is part of the treasure map!",
#     ],
#     Action.ENTER: ["You entered the Black Citadel. Good luck!"],
# }
#
# # These blocks contain the pieces of the treasure map
# game_treasure_map_blocks: List[int] = [5, 9]
#
#
# def game():
#     game_start()
#
#     position = 0  # the position of the player
#     has_entered = False  # whether the player has entered the citadel
#     num_treasure_map_piece = 0  # the number of treasure map pieces
#     investigated = [False] * 10  # whether a block has been investigated
#     is_game_over = False  # whether the game is over
#
#     while not is_game_over:
#         block_name = game_block_names[position]
#         actions = game_actions[position]
#
#         print(f"\nYou are at the {block_name}.")
#         prompt_actions(actions)
#         if num_treasure_map_piece == 2:
#             print("Something is chasing you. You must leave the citadel ASAP.")
#
#         # Let player input an action word
#         action_word = input("What will you do > ").lower()
#         action = convert_action_word(action_word, actions)
#         if action == -1:
#             continue
#
#         # Print the prompting text
#         print_prompting_text(action, position, investigated)
#
#         # If the action is Action.INVESTIGATE, check if the block contain the pieces of treasure map
#         if action == Action.INVESTIGATE and not investigated[position]:
#             if position in game_treasure_map_blocks:
#                 num_treasure_map_piece += 1
#                 print("You tuck the piece of the treasure map into your pocket.")
#             investigated[position] = True
#
#             # If two pieces of treasure map are gathered
#             if num_treasure_map_piece == 2:
#                 print(
#                     "You've collected all the pieces of the treasure map. Time to ESCAPE!!!"
#                 )
#
#         # Change the current position
#         position = change_position(position, action)
#         if position > 0:
#             has_entered = True
#
#         # If the position is 0, which is at the entrance of the citadel, and the player has entered
#         # the citadel, the game is over
#         if has_entered and position == 0:
#             game_over(num_treasure_map_piece)
#             is_game_over = True
#
#     # End the program
#     exit(0)
#
#
# def game_start():
#     """Prints the backstory and the starting prompt."""
#     print(
#         "In the land of whimsy and wonder, there stands the Black Citadel, and old, "
#         "spooky citadel haunted ghost. These wandering spirits were once brave soldiers who "
#         "fought in an intense war a long time ago. Legend has it that somewhere inside the "
#         "citadel, there is an awesome treasure map to be discovered! Loads of daring adventurers "
#         "have come to Black Citadel, all excited to find the treasure map. However, nobody has "
#         "ever made it out of there!"
#     )
#     print(
#         "Now you are standing at the entrance of the Black Citadel. You can either enter the "
#         "Black Citadel or turn back."
#     )
#
#
# def prompt_actions(actions: List[int]):
#     """Prints a string that describes the given actions."""
#     prompts = [game_action_prompts[action] for action in actions]
#
#     if len(prompts) > 1:
#         prompts[-1] = "or " + prompts[-1]
#
#     prompt_text = ", ".join(prompts)
#     print(f"You can {prompt_text}.")
#
#
# def convert_action_word(action_word: str, actions: List[int]) -> int:
#     """Converts an action word into corresponding action.
#     :param action_word: The action word to convert
#     :param actions: Available actions.
#     :return: The corresponding action; -1 if the action_word or action is invalid
#     """
#     # Check if the action word is valid
#     if action_word not in game_word_action_dict:
#         print(f"Invalid action: {bold(action_word)}")
#         return -1
#
#     # Get the corresponding action (int)
#     action = game_word_action_dict[action_word]
#
#     # Check if the action is valid
#     if action not in actions:
#         print(f"Invalid action: {bold(action_word)}")
#         return -1
#
#     return action
#
#
# def print_prompting_text(action: int, position: int, investigated: List[bool]):
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
#     if action in game_scripts:
#         text_list = game_scripts[action]
#         if len(text_list) > position and text_list[position] is not None:
#             print(text_list[position])
#     else:
#         # Head to another block
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
#     """Processes game over.
#     :param treasure_map_piece_num: The number of treasure map pieces the player gathered.
#     """
#     print()
#     if treasure_map_piece_num == 0:
#         print("You haven't found the treasure map ...")
#     elif treasure_map_piece_num == 1:
#         print("You haven't found all pieces of the treasure map ...")
#     elif treasure_map_piece_num == 2:
#         print("You've found the treasure map. It's time to embark on a new journey.")
#
#     # Print author's information
#     print("\n" + "=" * 40 + " Game Over " + "=" * 40 + "\n")
#     print("Game name: The Black Citadel v1.1")
#     print("Author: James Chan")
#     print("Creation date: Sep 17, 2023")
#     print(
#         "Special Thanks: ChatGPT helped me refine the backstory and room descriptions"
#     )
#
#
# # Start the game
# game()
