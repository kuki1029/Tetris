import pygame
from tetris_game import tetris
pygame.init()
pygame.font.init()

# Constant colors
DARKBLUE = (34, 28, 52)

# Main function for calling all the games functions and starting the game
def main():

    # Sets screen size, bg color and caption for window
    screen = pygame.display.set_mode((800, 600))
    screen.fill(DARKBLUE)
    pygame.display.set_caption("Tetris")

    # Creates object from class
    tetrisGame = tetris(screen)

    # Main while loop for all of games functions
    run = True
    while run:

        # Closes pygaem window if exit is clicked by user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        tetrisGame.draw_background()
        pygame.display.update()




main()
