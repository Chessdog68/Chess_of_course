import math
import time

class pieces:
    def __init__(self, type, pos_x, pos_y):
        self.type = type
        self.position = (pos_x, pos_y)
        self.name = f"{self.type}"




   








def board(self, position):
        self.position = position
        for i in range(1, 9):
            print(" ---" * 8)
            for j in range(1, 9):
                if (i, j) == self.position:
                    print(f"| {self.type} ", end="")
                else:
                    print("|   ", end="")
            print("|")
        print(" ---" * 8)


def player_1(pieces):
    
     print("Player 1\n where would you like the king?:")
   # print("x: ")
     x = int(input("x: "))
   #  print("y: ")
     y = int(input("y: "))

     white_king = pieces("wk", x, y)
     board(white_king, white_king.position)
     return white_king
    
     
def player_2(pieces):
    
     print("Player 2\n where would you like the black king?:")
   # print("x: ")
     x = int(input("x: "))
    # print("y: ")
     y = int(input("y: "))

     black_king = pieces("", x, y)
     return black_king


def game():
   while (1):
    player_1(pieces)
    player_2(pieces)
   

game()
