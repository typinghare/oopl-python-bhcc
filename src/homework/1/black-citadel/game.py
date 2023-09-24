"""Main game."""
import action
import block
import interact

# [Basic Info]
# Name: Black Citadel
# Version: v1.2
# Environment: Python 3.11.4; macOS 13.4.2_1
#
# [About the Game]
# In the land of whimsy and wonder, there stands the Black Citadel, and old, spooky citadel haunted
# with ghosts. These wandering spirits were once brave soldiers who fought in an intense war a long
# time ago. Legend has it that somewhere inside the citadel, there is an awesome treasure map to
# Black Citadel, all excited to find the treasure map. However, nobody has ever made it out of
# there!
#
# The structure of the Black Citadel is simple. It can be divided in 11 blocks:
# ===============
# || 7 | 8 | 9 ||   ==> 3rd floor
# || 4 | 5 | 6 ||   ==> 2nd floor
# || 1 | 2 | 3 ||   ==> 1st floor
# ===============
#      | 0 |        (The hidden room (10) is inside the block (9))
#
# Now, you (the player) is standing at the entrance of the Black Citadel (position 0).


def start():
    """Starts the game."""

    # Print the backstory and the game starting prompt
    print(
        "In the land of whimsy and wonder, there stands the Black Citadel, and old, "
        "spooky citadel haunted ghost. These wandering spirits were once brave soldiers who "
        "fought in an intense war a long time ago. Legend has it that somewhere inside the "
        "citadel, there is an awesome treasure map to be discovered! Loads of daring adventurers "
        "have come to Black Citadel, all excited to find the treasure map. However, nobody has "
        "ever made it out of there!\n"
        "Now you are standing at the entrance of the Black Citadel. You can either enter the "
        "Black Citadel or turn back."
    )

    position = 0  # the index of the block where the player is
    has_entered = False  # whether the player has entered the citadel
    num_treasure_map_piece = 0  # the number of treasure map pieces
    investigated = [False] * len(block.names)  # whether a block has been investigated
    is_game_over = False  # whether the game is over
    num_investigation = 0  # The total number of times of investigation

    def is_spectre_chasing():
        """
        Whether the spectre is chasing the player.
        :return: true if the spectre is chasing the player.
        """
        return (
            num_treasure_map_piece >= action.max_investigation
            or num_treasure_map_piece >= 2
        )

    while not is_game_over:
        print(
            f"\nYou are at the {block.names[position]}. {block.descriptions[position]}"
        )
        if is_spectre_chasing():
            print("Something is chasing you. You must leave the citadel ASAP.")

        player_action, action_str = interact.input_action()
        if (
            player_action == action.Action.INVALID
            or player_action not in action.available[position]
        ):
            print(f"Unavailable action: {action_str}.")
            continue

        # Print script if it is not an empty string
        script = action.get_script(player_action, position)
        if player_action == action.Action.INVESTIGATE:
            if investigated[position]:
                script = "You've investigated this room. You should move on to the next room."
            elif is_spectre_chasing():
                print(
                    "You are caught by a huge spectre. You are smothered and gradually lose "
                    "consciousness."
                )
                print_game_information()
            else:
                # Check if the block contain the pieces of the treasure map
                num_investigation += 1

                if position in block.treasure_maps:
                    num_treasure_map_piece += 1
                    script += (
                        "\nYou tuck the piece of the treasure map into your pocket."
                    )
                investigated[position] = True

                # If two pieces of treasure map are gathered
                if num_treasure_map_piece == 2:
                    script += (
                        "\nYou've already collected all the pieces of the treasure map. "
                        "ESCAPE!!!"
                    )
        if script != "":
            print(script)

        # Mark has_entered as true if the player entered the citadel; introduce the rules of game
        if position > 0 and not has_entered:
            has_entered = True

        # Change the position
        position = block.change_position(position, player_action)

        # If the position is 0, which is at the entrance of the citadel, and the player has entered
        # the citadel, the game is over
        if has_entered and position == 0:
            is_game_over = True

    # Different numbers of treasure map pieces lead to different endings
    game_over(num_treasure_map_piece)


def game_over(num_treasure_map_piece: int):
    """Processes game over
    :param num_treasure_map_piece: The number of treasure map pieces the player gathered.
    """
    print()
    if num_treasure_map_piece == 0:
        print("You haven't found the treasure map ...")
    elif num_treasure_map_piece == 1:
        print("You haven't found all pieces of the treasure map ...")
    elif num_treasure_map_piece == 2:
        print("You've found the treasure map. It's time to embark on a new journey.")

    print_game_information()


def print_game_information():
    """Prints game information and exists the game."""
    print("\n" + "=" * 40 + " Game Over " + "=" * 40 + "\n")
    print("Game name: Black Citadel v1.2")
    print("Author: James Chan")
    print("Creation date: Sep 24, 2023")
    print(
        "Special Thanks: ChatGPT helped me refine the backstory and room descriptions"
    )

    # Exit the game
    exit(0)
