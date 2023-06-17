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

    size = 5
    num_of_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    # print("Welcome! Les play!\n")
    # player_name = input("Enter your name: \n")

    computer_board = Board(size, "Computer", num_of_ships, "computer")
    player_board = Board(size, "player", num_of_ships, "player")

    populate_board(computer_board)
    populate_board(player_board)


    # play_game(player_board, computer_board)

def play_game(player, computer):
    pass

def populate_board(board):
    
    
    while len(board.ships) < board.num_of_ships:
        try:
            x = random_size(board.size)
            y = random_size(board.size)
            for i in range(len(board.ships)):
                if board.ships[i] == [x, y]:
                    raise StopIteration
        except StopIteration:
            continue
        board.ships.append([x, y])
    
    print(board.ships)
    
    
    
        
    


def make_guess():
    pass

def validate_coordinates(x, y):
    pass


    

new_game()


