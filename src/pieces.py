
# FILE « ALPHABETICAL COLUMNS SPANNING LEFT TO RIGHT
# RANK « NUMBERED ROWS SPANNING FROM THE PLAYER UP

FIRST_RANK = "P" 
SECOND_RANK = [
        Piece()
        "R", "N", "B", "Q", "K", "B", "N", "R"]

class Square:
    def __init__(self, notation, color):
        self.notation = notation
        self.color = color
        self.piece = "empty"
        

class Chessboard:
    def __init__(self):
        self.RANKS = ["8", "7", "6", "5", "4", "3", "2", "1"]
        self.FILES = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.rows = []
        self.board = []
        for rank in self.RANKS:
            j = self.RANKS.index(rank) % 2
            for file in self.FILES:
                i = self.FILES.index(file)
                notation = file + rank
                if i % 2 == 0 and j == 0:
                    color = "white"
                elif i % 2 == 0 and j == 1:
                    color = "black"
                elif i % 2 == 1 and j == 0:
                    color = "black"
                elif i % 2 == 1 and j == 1:
                    color = "white"
                else:
                    color = "Error attributing color."
                self.rows.append(Square(notation, color))
            self.board.append(self.rows)
            self.rows = []
    
    def reset_chessboard(self):
        for piece_index in range(8):
            black_square = self.board[1][piece_index]
            black_square.piece = Piece(piece_index, black_square.notation, "black", FIRST_RANK)

            white_square = self.board[6][piece_index]
            white_square.piece = Piece(piece_index, white_square.notation, "white", FIRST_RANK)
        for piece in SECOND_RANK:
            self.board[0][SECOND_RANK.index(piece)].piece = Piece(0, 
            self.board[7][SECOND_RANK.index(piece)].piece = 

    def move(start, end):
        pass

    def show(self):
        for row in self.board:
            for square in row:
                print(f"{square.notation}. {square.piece.name}")


#delete late:
board = Chessboard()

class Piece:
    def __init__(self, index, position, color, name):
        self.index = index
        self.position = position
        self.last_position = position
        self.color = color
        self.name = name


