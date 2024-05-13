class GameMaster:
    def __init__(self, p1_char, p2_char):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player1_character = p1_char
        self.player2_character = p2_char
        self.player_turn = 1
        self.player_move = -1
        self.diagonals = [2, 6, 4, 0, 8]

    def win_check(self, play):
        # If a diagonal is chosen then check diagonals too, otherwise just check horizontal/vertical
        diagonal = False
        if play in self.diagonals:
            horizontal = self.check_horizontal(play)
            vertical = self.check_vertical(play)
            diagonal = self.check_diagonal(play)
        else:
            horizontal = self.check_horizontal(play)
            vertical = self.check_vertical(play)

        return True in [horizontal, vertical, diagonal]

    def check_horizontal(self, p):
        # Check values on the same row to see if they're all the same
        values = [p]  # List of values to check, adding chosen move
        r = p // 3 * 3  # Row offset

        # Calculate the other 2 positions to check on the same row as the player's choice
        for i in range(1, 3):
            values.append((p + i) % 3 + r)

        return self.board[values[0]] == self.board[values[1]] == self.board[values[2]]

    def check_vertical(self, p):
        # Check values in the same column to see if they're all the same
        values = [p]  # List of values to check, adding chosen move

        # Calculate the other 2 positions to check in the same column as the player's choice
        for i in range(1, 3):
            values.append((p + 3 * i) % 9)

        return self.board[values[0]] == self.board[values[1]] == self.board[values[2]]

    def check_diagonal(self, p):
        # Check values in the diagonals for 3 in a row
        # There are only 2 diagonals, so it's just easier to hard code those

        if (self.board[self.diagonals[0]] == self.board[self.diagonals[1]] == self.board[self.diagonals[2]]
                or self.board[self.diagonals[2]] == self.board[self.diagonals[3]] == self.board[self.diagonals[4]]):
            return True
        else:
            return False

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
        player_move = input(f"Player {self.player_turn + 1}, what's your move? ")

    def update_board(self):
        p = self.player_move
        player = self.player_turn

        # Update board and check for winning move
        if player == 1:
            self.board[p] = self.player1_character
        elif player == 2:
            self.board[p] = self.player2_character

        # If winning move: break game loop, else advance to next player turn
        if self.win_check(p):
            return False
        else:
            self.next_turn()
            return True

    def next_turn(self):
        self.player_turn = self.player_turn % 2 + 1

    def is_move_valid(self, position):
        try:
            p = int(position) - 1
        except ValueError:
            print("Please enter a number 1-9.")
            return False

        if self.board[p] == "x" or self.board[p] == "o":
            print("That position has already been chosen. Please choose a valid position")
            return False
        else:
            self.player_move = p
            return True
