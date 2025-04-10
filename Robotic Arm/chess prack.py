class Piece:
    def __init__(self, type, pos_x, pos_y):
        self.type = type
        self.position = (pos_x, pos_y)
        self.name = f"{self.type}"


def board(white_piece, black_piece):
    for i in range(1, 9):
        print(" ---" * 8)
        for j in range(1, 9):
            if (i, j) == white_piece.position:
                print(f"| {white_piece.type} ", end="")
            elif (i, j) == black_piece.position:
                print(f"| {black_piece.type} ", end="")
            else:
                print("|   ", end="")
        print("|")
    print(" ---" * 8)


def player_1():
    print("Player 1\n Where would you like the white king?")
    x = int(input("x: "))
    y = int(input("y: "))
    white_king = Piece("wk", x, y)
    return white_king


def player_2():
    print("Player 2\n Where would you like the black king?")
    x = int(input("x: "))
    y = int(input("y: "))
    black_king = Piece("bk", x, y)
    return black_king


def game():
    white_king = player_1()
    black_king = player_2()
    while True:
        board(white_king, black_king)
        print("Player 1's turn to move the white king")
        white_king.position = (int(input("New x: ")), int(input("New y: ")))
        board(white_king, black_king)
        print("Player 2's turn to move the black king")
        black_king.position = (int(input("New x: ")), int(input("New y: ")))


game()