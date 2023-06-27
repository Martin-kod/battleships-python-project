from random import randint


class Board:
    """
    Creating Board class to include properties like size, number of ships,
    name, type, as well as a list of lists for the board and empty lists for
    guesses and ships.

    Code in class written by Code Institute Battleships tutorial.
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
    """
    Creates a random number between 0 and size, which will later be set to 5

    Code in function written by Code Institute Battleships tutorial.
    """
    return randint(0, size - 1)


def new_game():
    """
    Sets values to number of ships and size and briefs user how to start
    and play the game. Creates two instances of the class Board and populates
    these with ships by calling the function. Also calls function for playing
    the game.

    Code in function written by Code Institute Battleships tutorial.
    """

    size = 5
    num_of_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcome! Let's play some Battleships!!\n")
    print("Board size: 5. Number of ships: 4")
    print("Ship size: 1")
    print("Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Enter your name: \n")

    computer_board = Board(size, "Computer", num_of_ships, "computer")
    player_board = Board(size, player_name, num_of_ships, "player")

    populate_board(computer_board)
    populate_board(player_board)

    play_game(player_board, computer_board)


def play_game(player_board, computer_board):
    """
    The main game function which renders the game boards, calls the
    make_guess and validate_coordinate functions in order to use these
    in the game. Increases scores and adds coordinate values to guesses.
    The function is a loop so as to continue playing with a prompt option
    to break.
    """
    for i in player_board.ships:
        player_board.board[i[0]][i[1]] = "@"

    play_again = True
    while play_again:

        print("-" * 35)

        print(f"{player_board.name}'s board")

        for i in player_board.board:
            print(*i, sep=" ")

        print("-" * 35)
        print("Computer's board")

        for i in computer_board.board:
            print(*i, sep=" ")

        print("-" * 35)

        print("\n")

        player_guess_validation = False
        while player_guess_validation is False:
            player_guess = make_guess(player_board)
            x, y = player_guess
            player_guess_validation = validate_coordinates(x, y, player_board)
        player_board.guesses.append([int(x), int(y)])

        computer_guess_validation = False
        while computer_guess_validation is False:
            computer_guess = make_guess(computer_board)
            x, y = computer_guess
            computer_guess_validation = validate_coordinates(x, y, computer_board)
        computer_board.guesses.append([x, y])

        player_score = False
        print(f"You guessed: {player_board.guesses[-1]}")
        for i in range(len(computer_board.ships)):
            computer_ship = computer_board.ships[i]
            if computer_ship == player_board.guesses[-1]:
                computer_board.board[computer_ship[0]][computer_ship[1]] = "*"
                scores["player"] += 1
                print(f"You hit one of the computer's battleships!")
                player_score = True

        if player_score is False:
            print("You missed.")
            latest_guess = player_board.guesses[-1]
            computer_board.board[latest_guess[0]][latest_guess[1]] = "X"

        computer_score = False
        print(f"Computer guessed: {computer_board.guesses[-1]}")
        for i in range(len(player_board.ships)):
            player_ship = player_board.ships[i]
            if player_ship == computer_board.guesses[-1]:
                player_board.board[player_ship[0]][player_ship[1]] = "*"
                scores["computer"] += 1
                print(f"Computer hit one of your battleships!")
                computer_score = True

        if computer_score is False:
            print("Computer missed.")
            latest_guess = computer_board.guesses[-1]
            player_board.board[latest_guess[0]][latest_guess[1]] = "X"

        print("-" * 35)
        print("The scores are:")
        print(f"{player_board.name}: {scores['player']}, Computer: {scores['computer']}")
        print("-" * 35)

        if scores["computer"] > 3 and scores["player"] > 3:
            print("It's a tie!")
            print("Thanks for playing!")
            break
        elif scores["computer"] > 3:
            print("Sorry, you lost")
            print("Thanks for playing!")
            break
        elif scores["player"] > 3:
            print("Congratulations! You won!!")
            print("Thanks for playing!")
            break

        quit_game = False
        game_continue = False
        while game_continue is False:
            key_for_continue = input(
                "Do you want to continue? y/n \n")
            try:
                if key_for_continue == "n":
                    quit_game = True
                    break
                elif key_for_continue == "y":
                    game_continue = True
            except ValueError:
                print("That was not one of the options!")

        if quit_game is True:
            print("Thanks for playing!")
            break


def populate_board(board):
    """
    Random positioning of the battleships.
    """
    while len(board.ships) < board.num_of_ships:
        x = random_size(board.size)
        y = random_size(board.size)
        for i in range(len(board.ships)):
            if board.ships[i] == [x, y]:
                continue
        board.ships.append([x, y])


def make_guess(board):
    """
    Making guesses through prompts as user and
    random function for computer.
    """
    if board.type == "player":
        x = input('Guess row\n')
        y = input('Guess column\n')
        return (x, y)

    if board.type == "computer":
        x = random_size(board.size)
        y = random_size(board.size)
        return (x, y)


def validate_coordinates(x, y, board):
    """
    Validates guesses through exception handling.
    Gives printed statements to guide the user.
    """

    if board.type == "player":
        try:
            int_x = int(x)
            int_y = int(y)
        except ValueError:
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
                if board.guesses[i] == [x, y]:
                    raise ValueError
        except ValueError:
            return False
        return True


new_game()
