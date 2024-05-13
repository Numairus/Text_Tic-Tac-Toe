from game_master import GameMaster

if __name__ == '__main__':
    # Initial setup: Setting player characters, initialize game master
    player1_character = "x"
    player2_character = "o"
    character_choice = input("Player 1, would you like to be 'x' or 'o'? ")
    if character_choice == "o":
        player1_character = "o"
        player2_character = "x"

    game_master = GameMaster(player1_character, player2_character)
    print(f"Player 1 is {player1_character}")
    print(f"Player 2 is {player2_character} ")

    # Game loop
    while True:
        # Increment/alternate player turn
        # Draw board
        # Get player move input
        # Update board with given player move input

        game_master.next_turn()
        print(f"Turn {game_master.player_turn}")
        game_master.draw_board()
        player_move = input(f"Player {game_master.player_turn}, what's your move? ")
        game_master.update_board(player_move)


