"""Main module."""
import game

# Start the game
try:
    game.start()
except KeyboardInterrupt:
    print("\nBye.")
    exit(0)
