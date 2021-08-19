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
        # Describes the position of the current moving block
        self.xPos = 4
        self.yPos = 0

        # These two arrays hold the current and next shape
        self.currentShape = shapes[random.randint(0, 6)]
        self.nextShape = shapes[random.randint(0, 6)]

        # This lets the game know if the block has landed or reached the bottom
        self.landed = False

        # The gameboard array
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
                     [0, 0, 0, 0, 0, 0, 0, 0,0, 0],
                     [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 3, 3, 2, 0, 0, 0],
                     [1, 1, 1, 1, 1, 4, 1, 2, 2, 0],
                     [1, 1, 6, 6, 3, 3, 4, 2, 2, 0],
                     [0, 1, 1, 1, 7, 4, 4, 2, 1, 0],
                     [1, 1, 1, 1, 7, 7, 4, 2, 1, 1] ]
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

        # Dimensions of the gameboard
        self.width = len(self.gameBoard[0])
        self.length = len(self.gameBoard)

        # Keeps track of how many loops are done
        self.loopCounter = 0

        # Variables related to holding a piece
        self.heldPiece = [[0]]
        self.currentlyHolding = False
        self.canHoldAgain = True

        # Boolean to see if board is being cleared
        self.isItBeingCleared = False

        # Falling speed varialbes
        self.fallingSpeed = 10

        # Score variables
        self.score = 90
        self.scoreMultiplier = 1

    # Runs some of the games main functions here
    def gameLoop(self):
        if not self.isItBeingCleared:
            # Moves the block down slowly buy allows to move sideways or rotate faster
            if self.loopCounter > self.fallingSpeed:
                self.hasItLanded()
                self.movePieceDown()
                self.loopCounter = 0
        else:
            if self.loopCounter > 5:
                self.clearBoard()
                self.score += 10 * self.scoreMultiplier
                self.scoreMultiplier += 1
                if not self.canBoardBeCleared():
                    self.isItBeingCleared = False
                    self.canHoldAgain = True
                    self.spawn_piece()
                    if self.score < 100:
                        self.scoreMultiplier = 1
                    elif self.score < 1000:
                        self.scoreMultiplier = 5
                    else:
                        self.scoreMultiplier = 10
                self.loopCounter = 0
                if self.score < 100:
                    self.fallingSpeed = 10
                elif self.score < 1000:
                    self.fallingSpeed = 5
                else:
                    self.fallingSpeed = 2

        self.loopCounter += 1

    # Will spawn a piece if a piece doesn't already exist and hasn't landed
    def spawn_piece(self):
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
            if not self.canBoardBeCleared():
                self.canHoldAgain = True
                self.spawn_piece()
            else:
                self.isItBeingCleared = True


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

    #Hold piece
    def holdPiece(self):
        # This first one checks if it is the first time the user is holding a piece
        # We need this as we cannot replace the current piece with an empty piece
        if self.heldPiece == [[0]]:
            self.canHoldAgain = False
            self.heldPiece = self.currentShape[:]
            self.spawn_piece()

        # Checks if user is allowed to hold again or not according to tetris rules
        elif self.canHoldAgain:
            self.canHoldAgain = False
            self.tempPiece = self.currentShape[:]
            self.currentShape = self.heldPiece[:]
            self.heldPiece = self.tempPiece[:]
            self.nextShape = shapes[random.randint(0, 6)]
            # If the shapes is the straight line, then we start the piece a bit lower.
            self.xPos = 4
            self.yPos = 0

    # Will clear board
    def clearBoard(self):
        for row in reversed(range(len(self.gameBoard))):
            if self.checkRow(row):
                del self.gameBoard[row]
                self.gameBoard.insert(0,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                break


    #checks if anything can be cleared on the board and returns a bool
    def canBoardBeCleared(self):
        for row in range(len(self.gameBoard)):
            if self.checkRow(row):
                return True
        return False

    # Checks if the row needs to be cleared or not
    def checkRow(self, row):
        for col in range(len(self.gameBoard[0])):
            if self.gameBoard[row][col] == 0:
                return False
        return True

    #Make the block fall faster
    def fallFaster(self, pressed):
        if pressed:
            self.fallingSpeed = 1
        else:
            self.fallingSpeed = 10

    # This determines the position where the block would fall hypothetically
    def hypotheticalFallLocation(self):
        tempYpos = self.yPos

        # These are checks to see if the hypothetical block has landed
        for y in range(tempYpos, len(self.gameBoard)):
            row = (len(self.currentShape) - 1)
            for col in range(len(self.currentShape[0])):
                if y + len(self.currentShape) >= self.length:
                    return [self.xPos, y]
                elif self.currentShape[row][col] != 0 and self.gameBoard[y + len(self.currentShape)][
                    self.xPos + col] != 0:
                    return [self.xPos, y]
                elif self.currentShape[row - 1][col] != 0 and self.gameBoard[y + len(self.currentShape) - 1][
                    self.xPos + col] != 0:
                    return [self.xPos, y]
                elif len(self.currentShape) >= 2 and self.currentShape[row - 2][col] != 0 and \
                        self.gameBoard[y + len(self.currentShape) - 2][self.xPos + col] != 0:
                    return [self.xPos, y]



    # Returns the position of the current piece so the main function can draw it.
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

    # Will return the held piece
    def getHeldPiece(self):
        return self.heldPiece

    # Returns if the board is being cleared
    def isBoardBeingCleared(self):
        return self.isItBeingCleared

    # Returns the score
    def scoreNum(self):
        return self.score

