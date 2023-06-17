from random import randint

class Board:
    """
    Creating Board class to include properties like size, number of ships,
    name, etc.
    """
    def __init__(self, size, name, num_of_ships, type):
        self.size = size
        self.name = name
        self.num_of_ships = num_of_ships
        self.type = type
        self.board = [["." for x in range(size)] for y in range(size)]
        self.guesses = []
        self.ships = []
        
scores = {"player": 0, "computer": 0}

def random_size(size):
    return randint(0, size - 1)

def new_game():
    pass

def play_game(player, computer):
    pass

def populate_board(board):
    pass

def make_guess():
    pass

def validate_coordinates(x, y):
    pass

