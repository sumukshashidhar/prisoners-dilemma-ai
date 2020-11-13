class Player:
    def __init__(self, idx):
        self.color = idx
        self.move = None


class GameEngine:
    def __init__(self):
        self.blue_player = Player("blue")
        self.red_player = Player("Red")
        return

    def start_game(self):
        print(self.display_message)

    def determine_outcome(self):
        move1 = self.blue_player.move
        move2 = self.red_player.move
        if move1 and move2:
            return 1.0
        elif (move1 and not move2) or (not move1 and move2):
            return 0.5
        else:
            return 0
        