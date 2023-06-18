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


    play_game(player_board, computer_board)

def play_game(player_board, computer_board):
    
    for i in player_board.ships:
        player_board.board[i[0]][i[1]] = "@"
        
    for i in player_board.board:
        print(*i, sep=" ")

    print("-" * 35)

    for i in computer_board.board:
        print(*i, sep=" ")

    print("\n")

    player_guess_validation = False
    while player_guess_validation == False:
        player_guess = make_guess(player_board)
        x, y = player_guess
        player_guess_validation = validate_coordinates(x, y, player_board)
    player_board.guesses.append([int(x), int(y)])

    computer_guess_validation = False
    while computer_guess_validation == False:
        computer_guess = make_guess(computer_board)
        x, y = computer_guess
        computer_guess_validation = validate_coordinates(x, y, computer_board)
    computer_board.guesses.append([x, y])

    player_score = False
    print(f"You guessed: {player_board.guesses[-1]}")
    for i in range(len(computer_board.ships)):
        if computer_board.ships[i] == player_board.guesses[-1]:
            scores["player"] += 1
            print(f"You hit one of the computer's battleships!")
            player_score = True

    if player_score == False:
        print("You missed.")
    
    computer_score = False
    print(f"Computer guessed: {computer_board.guesses[-1]}")
    for i in range(len(player_board.ships)):
        if player_board.ships[i] == computer_board.guesses[-1]:
            scores["computer"] += 1
            print(f"Computer hit one of your battleships!")
            computer_score = True

    if computer_score == False:
        print("Computer missed.")

    print("-" * 35)
    print("The scores are:")
    print(f"{player_board.name}: {scores['player']}, Computer: {scores['computer']}")
    print("-" * 35)
    


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
    

def make_guess(board):

    if board.type == "player":
        y = input('Guess row\n')
        x = input('Guess column\n')
        return (x, y)

    if board.type == "computer":
        x = random_size(board.size)
        y = random_size(board.size)
        return (x, y)


def validate_coordinates(x, y, board):
    
    if board.type == "player":
        try:
            int_x = int(x)
            int_y = int(y)
        except:
            print("Value has to be a number!")
            return False
        try:
            if int_x >= board.size or int_y >= board.size:
                raise ValueError(
                    "Too much! Values can't be larger than 4!"
                )
        except ValueError as e:
            print(e)
            return False
        try:
            for i in range(len(board.guesses)):
                    if board.guesses[i] == [int_x, int_y]:
                        raise ValueError
        except ValueError:
            print("Cannot guess the same coordinates twice!")
            return False
        
        return True
    else:
        pass

    if board.type == "computer":
        try:
            for i in range(len(board.guesses)):
                    if board.guesses[i] == [int_x, int_y]:
                        raise ValueError
        except ValueError:
            return False
        return True

new_game()


