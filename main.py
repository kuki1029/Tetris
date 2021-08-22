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
DARKBLUE = (17, 53, 149)
BLOCKCOLORS = [YELLOW, ORANGE, DARKBLUE, PURPLE, LIGHTBLUE, GREEN, RED]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.SysFont('segoeui', 30)
fontButton = pygame.font.SysFont('segoeui', 55)
fontMenu = pygame.font.SysFont('segoeui', 80)

# Creates the main screen and clock
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Creates object from class
tetrisGame = tetris()

# Bools for which screen has to be on


# Main function for calling all the games functions and starting the game
def main():
    mainLoop = True
    game = False
    menu = True
    helper = False
    credits = False
    pygame.display.set_caption("Tetris")

    while mainLoop:
        # Menu screen
        while menu:
            easter = False
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False
                    menu = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if pos[0] > 250 and pos[0] < 550:
                        if pos[1] > 200 and pos[1] < 280:
                            game = True
                            menu = False
                        elif pos[1] > 300 and pos[1] < 380:
                            helper = True
                            menu = False
                        elif pos[1] > 400 and pos[1] < 480:
                            credits = True
                            menu = False


            keys = pygame.key.get_pressed()
            if keys[pygame.K_t]:
                easter = True

            if pos[0] > 250 and pos[0] < 550:
                if pos[1] >200 and pos[1] < 280:
                    drawMenu(True, False, False, easter)
                elif pos[1] > 300 and pos[1] < 380:
                    drawMenu(False, True, False, easter)
                elif pos[1] > 400 and pos[1] < 480:
                    drawMenu(False, False, True, easter)
            else:
                drawMenu(False, False, False, easter)
            pygame.display.update()

        # Helping screen
        while helper:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False
                    helper = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = True
                        helper = False
            drawHelp()
            pygame.display.update()

        # Hinsielp screen
        while credits:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False
                    credits = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = True
                        credits = False
            drawCredits()
            pygame.display.update()

        # Main while loop for all of games functions
        while game:
            clock.tick(40)
            clearing = tetrisGame.isBoardBeingCleared()
            # Closes pygaem window if exit is clicked by user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False
                    game = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = True
                        game = False
                    if not clearing:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            tetrisGame.rotatePiece(False)
                        elif event.key == pygame.K_h:
                            tetrisGame.holdPiece()
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            tetrisGame.horizontalMovement(True)
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            tetrisGame.horizontalMovement(False)
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            tetrisGame.fallFaster(True)
                elif event.type == pygame.KEYUP and not clearing:
                    if event.key == pygame.K_DOWN:
                        tetrisGame.fallFaster(False)

            if not clearing:
                drawBackground()
                tetrisGame.gameLoop()
                drawBoard()
                drawNextPiece()
                drawHeldPiece()
                drawCurrentPiece()
                drawHypoPiece()
            else:
                drawBackground()
                tetrisGame.gameLoop()
                drawBoard()
                drawNextPiece()
                drawHeldPiece()
            #print(np.array(tetrisGame.get_gameboard()))
            pygame.display.update()



# Draws main features of the background including the outlines and text
def drawBackground():
    score = tetrisGame.scoreNum()

    screen.fill(DARKPURPLE)

    # Outline for blocks
    pygame.draw.rect(screen, lIGHTGRAY, (299, 79, 202, 402), 1)

    # Outline and text for next block box
    pygame.draw.rect(screen, lIGHTGRAY, (522, 120, 88, 80), 1)
    textsurface = font.render('NEXT', True, lIGHTGRAY)
    screen.blit(textsurface, (532, 84))

    # Outline and text for hold box
    pygame.draw.rect(screen, lIGHTGRAY, (190, 120, 88, 80), 1)
    textsurface = font.render('HOLD', True, lIGHTGRAY)
    screen.blit(textsurface, (195, 84))

    # Score text
    textsurface = font.render('SCORE: ' + str(score), True, lIGHTGRAY)
    screen.blit(textsurface, (300, 40))

# This takes in the tetris board array and draws in the colors according to the array
# The array uses different numbers to show which colors should go there.
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

# Draws in the current piece
def drawCurrentPiece():
    pos = tetrisGame.currentPos()
    shape = tetrisGame.getCurrentPiece()
    # If the y value of
    if pos[1] >= 1:
        for row in range(len(shape)):
            for col in range(len(shape[0])):
                if shape[row][col] != 0:
                    xBlock = 300 + (blockSize * pos[0]) + (blockSize * col)
                    yBlock = 40 + (blockSize * pos[1]) + (blockSize * row)
                    # This first if statement makes it so the block looks like it is coming out of the top of the border
                    if pos[1] == 1:
                        if row > 0:
                            pygame.draw.rect(screen, BLOCKCOLORS[(shape[row][col] - 1)], (xBlock, yBlock, blockSize, blockSize))
                    else:
                        pygame.draw.rect(screen, BLOCKCOLORS[(shape[row][col] - 1)] , (xBlock, yBlock, blockSize, blockSize))

# Draws in the next piece
def drawNextPiece():
    nextShape = tetrisGame.getNextPiece()
    for row in range(len(nextShape)):
        for col in range(len(nextShape[0])):
            if nextShape[row][col] != 0:
                # 566 is the X midpoint of the next outline and 160 is the Y midpoint
                xBlock = (blockSize * col) + 566 - ((len(nextShape[0]) / 2) * blockSize)
                yBlock = (blockSize * row) + 160 - (((len(nextShape)) / 2) * blockSize)
                pygame.draw.rect(screen, BLOCKCOLORS[(nextShape[row][col] - 1)], (xBlock, yBlock, blockSize, blockSize))

# Draws in the next piece
def drawHeldPiece():
    heldShape = tetrisGame.getHeldPiece()
    for row in range(len(heldShape)):
        for col in range(len(heldShape[0])):
            if heldShape[row][col] != 0:
                # 234 is the X midpoint of the next outline and 160 is the Y midpoint
                xBlock = (blockSize * col) + 234 - ((len(heldShape[0]) / 2) * blockSize)
                yBlock = (blockSize * row) + 160 - (((len(heldShape)) / 2) * blockSize)
                pygame.draw.rect(screen, BLOCKCOLORS[(heldShape[row][col] - 1)], (xBlock, yBlock, blockSize, blockSize))

# Draws the hypothetical position
def drawHypoPiece():
    hypoPos = tetrisGame.hypotheticalFallLocation()
    shape = tetrisGame.getCurrentPiece()
    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] != 0:
                xBlock = 300 + (blockSize * hypoPos[0]) + (blockSize * col)
                yBlock = 40 + (blockSize * hypoPos[1]) + (blockSize * row)
                pygame.draw.rect(screen, BLOCKCOLORS[(shape[row][col] - 1)], (xBlock, yBlock, blockSize, blockSize), 2)

def drawMenu(box1, box2, box3, easter):
    screen.fill(DARKPURPLE)

    # Tetris text
    textsurface = fontMenu.render("TETRIS", True, lIGHTGRAY)
    screen.blit(textsurface, (284, 40))

    # Play button
    if box1:
        pygame.draw.rect(screen, WHITE, (250, 200, 300, 80), 0, 10)
        textsurface = fontButton.render("Start Game!", True, BLACK)
        screen.blit(textsurface, (265, 200))
    else:
        pygame.draw.rect(screen, lIGHTGRAY, (250, 200, 300, 80), 2, 10)
        textsurface = fontButton.render("Start Game!", True, lIGHTGRAY)
        screen.blit(textsurface, (265, 200))


    # Help Button
    if box2:
        pygame.draw.rect(screen, WHITE, (250, 300, 300, 80), 0, 10)
        textsurface = fontButton.render("Help", True, BLACK)
        screen.blit(textsurface, (347, 297))
    else:
        pygame.draw.rect(screen, lIGHTGRAY, (250, 300, 300, 80), 2, 10)
        textsurface = fontButton.render("Help", True, lIGHTGRAY)
        screen.blit(textsurface, (347, 297))

    # Credits Button
    if box3:
        pygame.draw.rect(screen, WHITE, (250, 400, 300, 80), 0, 10)
        textsurface = fontButton.render("Credits", True, BLACK)
        screen.blit(textsurface, (327, 397))
    else:
        pygame.draw.rect(screen, lIGHTGRAY, (250, 400, 300, 80), 2, 10)
        textsurface = fontButton.render("Credits", True, lIGHTGRAY)
        screen.blit(textsurface, (327, 397))

    if easter:
        textsurface = font.render("You're amazing!", True, WHITE)
        screen.blit(textsurface, (300, 150))

# Draws the text in the help box
def drawHelp():
    screen.fill(DARKPURPLE)

    textsurface = font.render("Move Sideways: Left/Right arrow keys or A/D", True, WHITE)
    screen.blit(textsurface, (50, 50))
    textsurface = font.render("Rotate: Up arrow key or W", True, WHITE)
    screen.blit(textsurface, (50, 90))
    textsurface = font.render("Move Down Faster: Down arrow key or S", True, WHITE)
    screen.blit(textsurface, (50, 130))
    textsurface = font.render("Hold: Press H", True, WHITE)
    screen.blit(textsurface, (50, 170))
    textsurface = font.render("Pause: Escape key", True, WHITE)
    screen.blit(textsurface, (50, 210))
    textsurface = font.render("Easter Egg: I'd love to drink this.", True, WHITE)
    screen.blit(textsurface, (50, 245))


# Draws the credits
def drawCredits():
    screen.fill(DARKPURPLE)
    textsurface = fontButton.render("Made by Kunal Varkekar", True, WHITE)
    screen.blit(textsurface, (110, 100))
    textsurface = fontButton.render("with love.", True, WHITE)
    screen.blit(textsurface, (270, 160))
    textsurface = fontButton.render("19/08/2020", True, WHITE)
    screen.blit(textsurface, (250, 240))
    textsurface = font.render('"' + "Failure is the opportunity to ", True, WHITE)
    screen.blit(textsurface, (170, 340))
    textsurface = font.render("began again more intelligently" + '"', True, WHITE)
    screen.blit(textsurface, (230, 370))
    textsurface = font.render("-Henry Ford", True, WHITE)
    screen.blit(textsurface, (390, 399))


main()