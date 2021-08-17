import pygame
import numpy as np
from tetris_game import tetris
pygame.init()
pygame.font.init()

# Constants for dimensions
blockSize = 20

# Constant colors
DARKPURPLE = (34, 28, 52)
lIGHTGRAY = (232, 228, 236)
YELLOW = (249, 218, 30)
RED = (235, 12, 66)
LIGHTBLUE = (43, 168, 224)
PURPLE = (170, 27, 136)
GREEN = (2, 179, 74)
ORANGE = (253, 130, 1)
DARKBLUE = (17,53,149)
BLOCKCOLORS = [YELLOW, ORANGE, DARKBLUE, PURPLE, LIGHTBLUE, GREEN, RED]

# Fonts
font = pygame.font.SysFont('segoeui', 30)

# Creates the main screen and clock
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Creates object from class
tetrisGame = tetris()

# Main function for calling all the games functions and starting the game
def main():

    # Sets screen size, bg color and caption for window
    pygame.display.set_caption("Tetris")

    # Main while loop for all of games functions
    run = True
    while run:
        clock.tick(1)
        # Closes pygaem window if exit is clicked by user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawBackground()
        drawBoard()
        tetrisGame.gameLoop()
        drawCurrentPiece()
        #print(np.array(tetrisGame.get_gameboard()))
        pygame.display.update()



# Draws main features of the background including the outlines and text
def drawBackground():
    screen.fill(DARKPURPLE)

    # Outline for blocks
    pygame.draw.rect(screen, lIGHTGRAY, (299, 79, 202, 402), 1)

    # Outline and text for next block box
    pygame.draw.rect(screen, lIGHTGRAY, (522, 120, 88, 60), 1)
    textsurface = font.render('NEXT', True, lIGHTGRAY)
    screen.blit(textsurface, (532, 84))

    # Outline and text for hold box
    pygame.draw.rect(screen, lIGHTGRAY, (190, 120, 84, 60), 1)
    textsurface = font.render('HOLD', True, lIGHTGRAY)
    screen.blit(textsurface, (193, 84))

    # Score text
    textsurface = font.render('SCORE:' + ' 0', True, lIGHTGRAY)
    screen.blit(textsurface, (300, 40))

# This takes in the tetris board array and draws in the colors according to the array
# The array uses different numbers to show which colors should go there
def drawBoard():
    gameBoard = tetrisGame.get_gameboard()
    # This for loop starts at 2 as our board array has two extra spots on the top to allow the pieces to spawn properly
    for row in range(2, len(gameBoard)):
        for col in range(len(gameBoard[0])):
            # Checks if a piece is there
            if gameBoard[row][col] != 0:
                # 300 represents the left of the play area and 40 is the top y value. The top y value is actually 80 but
                # bcoz we start the for loop at 2 instead of 0, we need to compensate for it in the y values for the pieces
                pygame.draw.rect(screen, BLOCKCOLORS[(gameBoard[row][col] - 1)] , (300 + (blockSize * col), 40 + (blockSize * row), blockSize, blockSize))


def drawCurrentPiece():
    pos = tetrisGame.currentPos()
    shape = tetrisGame.getCurrentPiece()
    # If the y value of
    if pos[1] > 1:
        print(pos)
        for row in range(len(shape)):
            for col in range(len(shape[0])):
                if shape[row][col] != 0:
                    pygame.draw.rect(screen, BLOCKCOLORS[(shape[row][col] - 1)] , (300 + (blockSize * pos[0]) + (blockSize * col), 40 + (blockSize * pos[1]) + (blockSize * row), blockSize, blockSize))



main()
