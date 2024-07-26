BOARD = [1,2,3,4,5,6,7,8,9]
PLAYER_ONE_ICON = "🟢"
PLAYER_TWO_ICON = "🔴"
ROUND_COUNTER = 0
PLAYER_TURN = 1
MAX_ROUND = 9
GAME_ON = True
WINNING_COMBO = [
    # Check horizontal combinations
    [1,2,3],
    [4,5,6],
    [7,8,9],
    # Check vertical combinations
    [1, 4, 7],
    [2, 5, 6],
    [3, 6, 9],
    # Check diagonal combinations
    [1, 5, 9],
    [3, 5, 7],
]



# Welcome - VINCE
def welcome_screen():
    print("""
    Welcome to TTT
    
    """)

# Display and refreshing display - DAN
print()

# Getting player input

# Update display

# Check_Winner