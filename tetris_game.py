import pygame
import random


shapes = [
    [[1,1],
     [1,1]],

    [[2,0,0,0],
     [2,2,2,2]],

    [[0,0,0,3],
     [3,3,3,3]],

    [[0,4,0],
     [4,4,4]],

    [[5,5,5,5]],

    [[0,6,6],
     [6,6,0]],

    [[7,7,0],
     [0,7,7]]
]




class tetris:


    # Constructor
    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.currentShape = [[0]]
        self.landed = True
        self.gameBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
                     [0, 0, 6, 6, 3, 3, 4, 2, 2, 0],
                     [0, 6, 6, 7, 7, 4, 4, 2, 1, 1],
                     [5, 5, 5, 5, 7, 7, 4, 2, 1, 1], ]
        self.gameBoard2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]

    # Runs some of the games main functions here
    def gameLoop(self):
        self.spawn_piece()
        self.movePieceDown()


    # Will spawn a piece if a piece doesn't already exist and hasn't landed
    def spawn_piece(self):
        if self.landed:
            rand = random.randint(0, 6)
            self.currentShape = shapes[rand]
            # If the shapes is the straight line, then we start the piece a bit lower.
            self.xPos = 4
            self.yPos = 0
            self.landed = False



    # Will move the piece down on the board by increasing the y coordinates
    def movePieceDown(self):
        if not self.landed:
            self.yPos += 1
            print(self.yPos)

    # Does a check if the current moving piece has landed or not
    def hasItLanded(self):
        pass

    # Returns the position of the current piece so the main function can draw it
    def currentPos(self):
        return [self.xPos, self.yPos]

    # Will return the board array to the main function
    def get_gameboard(self):
            return self.gameBoard

    # Will return the current piece
    def getCurrentPiece(self):
            return self.currentShape

