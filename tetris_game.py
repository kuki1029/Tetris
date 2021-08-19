import pygame
import random
import numpy as np

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
        self.xPos = 4
        self.yPos = 0
        self.currentShape = shapes[random.randint(0, 6)]
        self.nextShape = shapes[random.randint(0, 6)]
        self.landed = False
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
                     [0, 0, 0, 0, 5, 6, 0, 0, 0, 0],
                     [0, 0, 0, 0, 4, 5, 0, 0, 0, 0],
                     [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 3, 3, 2, 0, 0, 0],
                     [0, 0, 0, 0, 0, 4, 1, 0, 0, 0],
                     [0, 0, 6, 6, 3, 3, 4, 2, 2, 0],
                     [0, 0, 0, 0, 7, 4, 4, 2, 1, 1],
                     [0, 0, 0, 0, 7, 7, 4, 2, 1, 1] ]
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
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.width = 10
        self.length = 22
        self.loopCounter = 0

    # Runs some of the games main functions here
    def gameLoop(self):
        self.spawn_piece()
        # Moves the block down slowly buy allows to move sideways or rotate faster
        if self.loopCounter > 5:
            self.hasItLanded()
            self.movePieceDown()
            self.loopCounter = 0
        self.loopCounter += 1


    # Will spawn a piece if a piece doesn't already exist and hasn't landed
    def spawn_piece(self):
        if self.landed:
            rand = random.randint(0, 6)
            self.currentShape = self.nextShape[:]
            self.nextShape = shapes[rand]
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
            if self.yPos + len(self.currentShape) >= self.length:
                self.landed = True
            elif self.currentShape[row][col] != 0 and self.gameBoard[self.yPos + len(self.currentShape)][self.xPos + col] != 0:
                self.landed = True
            elif self.currentShape[row - 1][col] != 0 and self.gameBoard[self.yPos + len(self.currentShape) - 1][self.xPos + col] != 0:
                self.landed = True
            elif len(self.currentShape) >= 2 and self.currentShape[row - 2][col] != 0 and self.gameBoard[self.yPos + len(self.currentShape) - 2][self.xPos + col] != 0:
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

    # Checks if it is possible to move the block to the left or the right
    # First we check if it is being moved outside the bounds
    def moveHorizontalPossible(self, toTheLeft):
        if self.xPos > 0 and self.xPos < self.width - (len(self.currentShape[0])):
            return self.hittingAnotherBlock(toTheLeft)
        elif self.xPos == 0 and not toTheLeft:
            return self.hittingAnotherBlock(toTheLeft)
        elif self.xPos == self.width - (len(self.currentShape[0])) and toTheLeft:
            return self.hittingAnotherBlock(toTheLeft)
        else:
            return False

    # Checks if another block is being hit when moving horizontally
    def hittingAnotherBlock(self, toTheLeft):
        if toTheLeft:
            for row in range(len(self.currentShape)):
                for col in range(len(self.currentShape[0])):
                    if self.currentShape[row][col] != 0:
                        if self.gameBoard[self.yPos + row][self.xPos + col - 1] != 0:
                            return False
                        break
            return True
        else:
            for row in range(len(self.currentShape)):
                for col in reversed(range(len(self.currentShape[0]))):
                    if self.currentShape[row][col] != 0:
                        if self.gameBoard[self.yPos + row][self.xPos + col + 1] != 0:
                            return False
                        break
            return True

    # Rotates the piece
    def rotatePiece(self, isItLeft):
        if self.rotateOutOfBounds():
            n = (len(self.currentShape))
            m = len(self.currentShape[0])
            newPiece = []
            for x in range(m):
                newPiece.append([])
                for y in range (n):
                    newPiece[x].append(0)
            for x in range(n):
                for y in range(m):
                    newPiece[y][n-1-x] = self.currentShape[x][y]
            if self.rotateIntoOtherBlock(newPiece):
                self.currentShape = newPiece[:]


    #Check if a rotate goes out of bounds
    def rotateOutOfBounds(self):
        if self.xPos + len(self.currentShape) > self.width:
            return False
        elif self.yPos + len(self.currentShape[0]) > self.length:
            return False
        else:
            return True

    def rotateIntoOtherBlock(self, newShape):
        for row in range(len(newShape)):
            for col in range(len(newShape[0])):
                if newShape[row][col] != 0 and self.gameBoard[self.yPos + row][self.xPos + col] != 0:
                    return False
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

    # Will return the new piece
    def getNextPiece(self):
        return self.nextShape

