from tile import tile
from copy import deepcopy
import random

class game:
    def __init__(self):
        self.board=[[tile(),tile(),tile(),tile()],[tile(),tile(),tile(),tile()],[tile(),tile(),tile(),tile()],[tile(),tile(),tile(),tile()]]
        self.rng=random.Random()
        self.score=0

    def __del__(self):
        self.board=[]

    def __copy__(self):
        return self

    def _move(self):
        for i in range(4):
            for j in range(3,-1,-1):
                if self.board[i][j].value==0:
                    self.board[i].pop(j)
                    self.board[i].append(tile())
        for i in range(4):
            for j in range(3):
                if self.board[i][j].value!=0:
                    if not self.board[i][j].is_joined():
                        if self.board[i][j].value==self.board[i][j+1].value:
                            self.board[i][j].join()
                            self.board[i][j+1].merge()
                            self.score+=self.board[i][j].value
        for i in range(4):
            for j in range(3,-1,-1):
                if self.board[i][j].value==0:
                    self.board[i].pop(j)
                    self.board[i].append(tile())

    def left(self):
        self._move()
        self.next_move()

    def right(self):
        for i in range(4):
            self.board[i].reverse()
        self._move()
        for i in range(4):
            self.board[i].reverse()
        self.next_move()

    def up(self):
        self.board=[list(x) for x in zip(*self.board)]
        self._move()
        self.board = [list(x) for x in zip(*self.board)]
        self.next_move()

    def down(self):
        self.board = [list(x) for x in zip(*self.board)]
        for i in range(4):
            self.board[i].reverse()
        self._move()
        for i in range(4):
            self.board[i].reverse()
        self.board = [list(x) for x in zip(*self.board)]
        self.next_move()

    def next_move(self):
        for i in range(4):
            for j in range(4):
                self.board[i][j].next_turn()

    def display(self):
        for i in range(4):
            for j in range(4):
                print(str(self.board[i][j].value)+"\t",end='')
            print()

    def game_over(self):
        print("lose")

    def place(self):
        free_space=False
        for i in range(4):
            for j in range(4):
                if self.board[i][j].value==0:
                    free_space=True

        if not free_space:
            self.game_over()
        else:
            placed=False
            while not placed:
                i=self.rng.randint(0,3)
                j=self.rng.randint(0,3)
                if self.board[i][j].value == 0:
                    placed=True
                    to_place=2
                    if self.rng.randint(0,9)==9:
                        to_place=4
                    self.board[i][j].place(to_place)

    def can_move(self):
        movable=False
        copied=deepcopy(self)
        copied.left()
        if str(copied.board)!=str(self.board):
            movable=True
        else:
            copied.right()
            if str(copied.board)!=str(self.board):
                movable = True
            else:
                copied.up()
                if str(copied.board)!=str(self.board):
                    movable = True
                else:
                    copied.down()
                    if str(copied.board)!=str(self.board):
                        movable = True
        return movable

a=game()
# a.place()
# a.place()
# a.place()
# a.place()
# a.place()
# a.place()
# a.place()
# a.place()
# a.place()
# a.place()
a.display()
# print("left")
# a.left()
# a.display()
# print("right")
# a.right()
# a.display()
# print("up")
# a.up()
# a.display()
# print("down")
# a.down()
# a.display()
# print("left")
# a.left()
# a.display()
#
#
# print(str(a.score))
print(str(a.can_move()))




