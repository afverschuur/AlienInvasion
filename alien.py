import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class representing an alien """

    def __init__(self, ai_game):
        """ Init alien and set starting position """
        super().__init__()
        self.screen = ai_game.screen

        # Load image and set rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact horizontal position
        self.x = float(self.rect.x)