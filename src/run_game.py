"""
Write docs
"""
from game import *


if __name__ == "__main__":
    instance = GameEngine()
    print("Welcome to the game")
    print("There are two playes")
    instance.play_move(1, "red")
    instance.play_move(0, "blue")
    print(instance.determine_outcome())