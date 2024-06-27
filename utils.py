#Contains utility functions like move parsing and displaying instructions.

def parse_move(move):
    try:
        from_square, to_square = move.split()
        return from_square, to_square
    except ValueError:
        return None

def display_instructions():
    print("Welcome to Anti-Chess!")
    print("Input moves in the form 'A2 B4'.")
    print("Commands:")
    print("  display - Display the current board")
    print("  quit - Quit the game (the other player wins)")
