class Player:
    def __init__(self, idx):
        self.color = idx
        self.move = None
        return

    def set_move(self, move):
        self.move = move
        return

    def get_move(self):
        return self.move


class GameEngine:
    def __init__(self):
        self.blue_player = Player("blue")
        self.red_player = Player("red")
        return

    def play_move(self, move, id):
        if id == "red":
            self.red_player.move = move
        else:
            self.blue_player.move = move

    def determine_outcome(self):
        move1 = self.blue_player.move
        move2 = self.red_player.move
        if move1 and move2:
            return 1.0, None
        elif move1 and not move2:
            return 0.5, self.blue_player.color
        elif not move1 and move2:
            return 0.5, self.red_player.color
        else:
            return 0, None
