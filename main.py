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
    print(f"Player 2 is {player2_character} ")

    player_turn = 1
    game_master.draw_board()

    # Game loop
    while True:
        # Get player move input
        # Update board with given player move input
        # Draw updated board
        # Increment/alternate player turn
        print(f"Turn {game_master.player_turn}")
        player_move = input(f"Player {player_turn}, what's your move? ")
        game_master.update_board(player_turn, player_move)
        game_master.draw_board()
        player_turn = player_turn % 2 + 1

