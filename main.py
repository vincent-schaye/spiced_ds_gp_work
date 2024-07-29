BOARD = [1, 2, 3, 4, 5, 6, 7, 8, 9]
PLAYER_ONE_ICON = "🔵"
PLAYER_TWO_ICON = "🔴"
CURRENT_ICON = ""
ROUND_COUNTER = 0
PLAYER_TURN = 1
MAX_ROUND = 9
GAME_ON = True
SCORE_1 = 0
SCORE_2 = 0
WINNING_COMBO = [
    # Check horizontal combinations9
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    # Check vertical combinations
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    # Check diagonal combinations
    [1, 5, 9],
    [3, 5, 7],
]

# ___________________________________________________________________________________________________________________

# Welcome Screen
def welcome_screen():
    print("""
    Welcome to TTT. First player to get 3-in-a-row Win!
    Press # Position on the Board to place your Piece
    Good Luck
    """)

# Check_Winner
def check_winner(BOARD, WINNING_COMBO):
    global GAME_ON, SCORE_1, SCORE_2
    result = []
    for combo in WINNING_COMBO:
        extracted = [BOARD[i - 1] for i in combo]
        if extracted == ["🔵", "🔵", "🔵"]:
            GAME_ON = False
            SCORE_1 += 1
            print(f"Player 1 Wins {PLAYER_ONE_ICON}, Current Score is {PLAYER_ONE_ICON}: {SCORE_1}, {PLAYER_TWO_ICON}: {SCORE_2}")
        elif extracted == ["🔴", "🔴", "🔴"]:
            GAME_ON = False
            SCORE_2 += 1
            print(f"Player 2 Wins {PLAYER_TWO_ICON}, Current Score is {PLAYER_ONE_ICON}: {SCORE_1}, {PLAYER_TWO_ICON}: {SCORE_2}")


# Display Board
def display_board():
    print(f"""
    {BOARD[0]} | {BOARD[1]} |  {BOARD[2]}\n
    {BOARD[3]} | {BOARD[4]} |  {BOARD[5]}\n
    {BOARD[6]} | {BOARD[7]} |  {BOARD[8]}\n
""")

# Controls global player turn switch
def switch_player_turn():
    global PLAYER_TURN
    PLAYER_TURN *= -1


# Getting player input - based on whose player turn it is.
# RETURNS player_choice (an integer from Board choice that remains)
def get_player_input():
    global PLAYER_TURN, CURRENT_ICON
    #Switches Current Icon so that place_icon_on_board function simply uses this to replace checker piece on baord
    if PLAYER_TURN == 1:
        CURRENT_ICON = PLAYER_ONE_ICON
    else:
        CURRENT_ICON = PLAYER_TWO_ICON

    while True:  # I want to keep re asking until player chooses the available numbers
        try:
            if PLAYER_TURN == 1:
                refine_player_name = 1
            else:
                refine_player_name = 2
            player_choice = int(input(f"Player {refine_player_name} ({CURRENT_ICON})'s turn, choose:  "))
            # print(player_choice)
            # print(type(player_choice))
            if player_choice in BOARD:
                return player_choice
            else:
                print("Invalid choice, number must be for available positions only")
        except ValueError:
            print("Please enter a numeric value")

    # find index and replace in BOARD

# Based on get_player_input() function, uses the return of player_choice to replace BOARD with checker piece of chosen position
# updates and displays board also
def place_icon_on_board(player_choice):
    global CURRENT_ICON
    player_choice -= 1
    BOARD[player_choice] = CURRENT_ICON
    # print("playerturn=",PLAYER_TURN)
    display_board()

def reset_game():
    global BOARD, SCORE_1, SCORE_2, GAME_ON, ROUND_COUNTER
    BOARD = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    SCORE_1 = 0
    SCORE_2 = 0
    ROUND_COUNTER = 0
    GAME_ON = True

def new_round():
    global BOARD, GAME_ON, ROUND_COUNTER
    BOARD = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ROUND_COUNTER = 0
    GAME_ON = True

def play_again_or_not():
    play_again_input = input("Play again? Or Reset? (Y/N/R): ").lower()
    if play_again_input == "y":
        new_round()
        play_game()
    elif play_again_input == "r":
        reset_game()
        play_game()
    elif play_again_input == "n":
        print("THANKS FOR PLAYING & GOODBYE!!👋👋")

def play_game():
    global GAME_ON
    while GAME_ON:
        global ROUND_COUNTER
        display_board()
        place_icon_on_board(get_player_input())  # displaying board also
        check_winner(BOARD, WINNING_COMBO)
        switch_player_turn()
        ROUND_COUNTER += 1
        if ROUND_COUNTER == 10:
            display_board()
            print("DRAW!!!")
            GAME_ON = False
    play_again_or_not()


# -----GAME --------------------#

welcome_screen()
play_game()




