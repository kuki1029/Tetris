import pygame
import random


shapes = [
    [[1,1],
     [1,1]],

    [[2,0,0],
     [2,2,2]],

    [[0,0,3],
     [3,3,3]],

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
        self.hasItLanded()
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

    # Does a check if the current moving piece has landed or not
    def hasItLanded(self):
        row = (len(self.currentShape) - 1)

        for col in range(len(self.currentShape[0])):
            if self.currentShape[row][col] != 0 and self.gameBoard[self.yPos + len(self.currentShape)][self.xPos + col] != 0:
                self.landed = True
            elif self.gameBoard[self.yPos + len(self.currentShape) - 1][self.xPos + col] != 0:
                self.landed = True
        if self.landed:
            self.addToBoard()


    # Adds the landed piece to the board
    def addToBoard(self):
        for row in range(len(self.currentShape)):
            for col in range(len(self.currentShape[0])):
                if self.currentShape[row][col] != 0:
                    self.gameBoard[self.yPos+row][self.xPos+col] = self.currentShape[row][col]

    # Moves the pieces left or right
    def horizontalMovement(self, toTheLeft):
        if self.moveHorizontalPossible(toTheLeft):
            if toTheLeft:
                self.xPos = self.xPos - 1
            else:
                self.xPos = self.xPos + 1
                print(self.xPos)

    # Checks if it is possible to move the block to the left or the right
    # First we check if it is being moved outside the bounds
    def moveHorizontalPossible(self, toTheLeft):
        if self.xPos > 0 and self.xPos < 10 - (len(self.currentShape[0])):
            print("S")
            return self.hittingAnotherBlock(toTheLeft)
        elif self.xPos == 0 and not toTheLeft:
            return self.hittingAnotherBlock(toTheLeft)
        elif self.xPos == 10 - (len(self.currentShape[0])) and toTheLeft:
            return self.hittingAnotherBlock(toTheLeft)
        else:
            return False

    # Checks if another block is being hit when moving horizontally
    def hittingAnotherBlock(self, toTheLeft):
        if toTheLeft:
            for row in range(len(self.currentShape)):
                for col in range(len(self.currentShape[0])):
                    if self.currentShape[row][col] != 0:
                        if self.gameBoard[self.yPos + row][self.xPos - 1] != 0:
                            print("A")
                            return False
                        break
            print("sss")
            return True
        else:
            for row in range(len(self.currentShape)):
                for col in reversed(range(len(self.currentShape[0]))):
                    if self.currentShape[row][col] != 0:
                        if self.gameBoard[self.yPos + row][self.xPos + len(self.currentShape[0])] != 0:
                            return False
                        break
            return True




    # Returns the position of the current piece so the main function can draw it
    def currentPos(self):
        return [self.xPos, self.yPos]

    # Will return the board array to the main function
    def get_gameboard(self):
            return self.gameBoard

    # Will return the current piece
    def getCurrentPiece(self):
            return self.currentShape

