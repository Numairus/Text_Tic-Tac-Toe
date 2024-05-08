class GameMaster:
    def __init__(self, p1_char, p2_char):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player1_character = p1_char
        self.player2_character = p2_char
        self.player_turn = 0

    def win_check(self, position):
        # Convert player position choice to board index
        i = position - 1
        # Check win conditions based on the last played position
        match position:
            case "1": # Top left corner
                # Check 2/3
                # Check 4/7
                # Check 5/9
                if (self.board[0] == self.board[1] == self.board[2]  # Top row
                        or self.board[0] == self.board[3] == self.board[6]  # Left column
                        or self.board[0] == self.board[4] == self.board[8]):  # Diagonal, top left to bottom right
                    return True
            case "2":
                # Check 1/3
                # Check 5/8
                if (self.board[0] == self.board[1] == self.board[2] # Top row
                        or self.board[1] == self.board[4] == self.board[7]): # Middle column
                    return True
            case "3":
                # Check 1/2
                # Check 6/9
                # Check 5/7
                pass
            case "4":
                # Check 1/7
                # Check 5/6
                pass
            case "5":
                # Check 4/6
                # Check 2/8
                # Check 1/9
                # Check 3/7
                pass
            case "6":
                # Check 4/5
                # Check 3/9
                pass
            case "7":
                # Check 1/4
                # Check 3/5
                # Check 8/9
                pass
            case "8":
                # Check 7/9
                # Check 2/5
                pass
            case "9":
                # Check 1/5
                # Check 7/8
                # Check 3/6
                pass
        pass

    def ai_play(self, character, move):
        self.board[move - 1] = character

    def draw_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")

    def player_turn(self):
        player_move = input(f"Player {self.player_turn() + 1}, what's your move? ")

    def update_board(self, player, position):
        i = int(position) - 1

        if player == 1:
            self.board[i] = self.player1_character
        elif player == 2:
            self.board[i] = self.player2_character
