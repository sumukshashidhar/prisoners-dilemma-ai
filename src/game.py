class Player:
    def __init__(self, idx):
        self.color = idx
        self.move = None

    def get_move(self):
        return self.move


class GameEngine:
    def __init__(self):
        self.blue_player = Player("blue")
        self.red_player = Player("Red")
        return

    def start_game(self):
        print(self.display_message)

    def determine_outcome(self):
        move1 =