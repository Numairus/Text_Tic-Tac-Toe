from game_master import GameMaster

if __name__ == '__main__':
    # Initial setup: Setting player characters, turn, and drawing game board
    player1_character = "x"
    player2_character = "o"
    character_choice = input("Player 1, would you like to be 'x' or 'o'? ")
    if character_choice == "o":
        player1_character = "o"
        player2_character = "x"

    game_master = GameMaster(player1_character, player2_character)
    print(f"Player 1 is {player1_character}")
    print(f"Player 2 is {player2_character} \n\n")

    player_turn = 1
    game_master.draw_board()

    # Game loop
    while True:
        pass

