# main Driver code

from board import Board
from utils import parse_move, display_instructions

def main():
    board = Board()
    current_player = 1

    display_instructions()

    while True:
        board.display()
        print(f"Player {current_player}'s turn")

        move = input("Enter your move (e.g., A2 B4) or command (display/quit): ").strip()

        if move.lower() == "display":
            board.display()
            continue

        if move.lower() == "quit":
            print(f"Player {3 - current_player} wins!")
            break

        if not parse_move(move):
            print("Invalid move format. Please use 'A2 B4' format.")
            continue

        from_square, to_square = parse_move(move)
        if board.move_piece(from_square, to_square, current_player):
            if board.is_winner(current_player):
                board.display()
                print(f"Player {current_player} wins!")
                break
            current_player = 3 - current_player
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
