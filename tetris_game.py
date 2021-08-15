import pygame

pygame.font.init()

class tetris:
    # Colors
    lIGHTGRAY = (232, 228, 236)

    # Fonts
    font = pygame.font.SysFont('segoeui', 30)

    # Constructor
    def __init__(self, screen):
        self.screen = screen

    # Draws main features of the background including the outlines and text
    def draw_background(self):

        # Outline for blocks
        pygame.draw.rect(self.screen, self.lIGHTGRAY, (300, 80, 200, 400), 1)

        # Outline and text for next block box
        pygame.draw.rect(self.screen, self.lIGHTGRAY, (522, 120, 84, 60), 1)
        textsurface = self.font.render('NEXT', True, self.lIGHTGRAY)
        self.screen.blit(textsurface, (532, 84))

        # Outline and text for hold box
        pygame.draw.rect(self.screen, self.lIGHTGRAY, (190, 120, 84, 60), 1)
        textsurface = self.font.render('HOLD', True, self.lIGHTGRAY)
        self.screen.blit(textsurface, (193, 84))

        # Score text
        textsurface = self.font.render('SCORE:'+' 0', True, self.lIGHTGRAY)
        self.screen.blit(textsurface, (300, 40))
