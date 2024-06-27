# Defines different chess pieces.

class Piece:
    def __init__(self, player):
        self.player = player

    def __str__(self):
        return self.symbol

class Pawn(Piece):
    symbol = "P"

class Knight(Piece):
    symbol = "N"

class Bishop(Piece):
    symbol = "B"

class Rook(Piece):
    symbol = "R"

class Queen(Piece):
    symbol = "Q"

class King(Piece):
    symbol = "K"
