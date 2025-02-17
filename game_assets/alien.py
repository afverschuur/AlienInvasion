import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class representing an alien """

    def __init__(self, game_base):
        """ Init alien and set starting position """
        super().__init__()
        self.game_base = game_base

        # Load image and set rect
        self.image = pygame.image.load('assets/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        # Store alien's exact horizontal position
        self.x = float(self.rect.x)
        #self.moving = False

    def update(self):
        """ Move the alien tot the right """
        #if self.moving:
        self.x += (self.game_base.settings.alien_speed * self.game_base.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ Return True is alien is at edge of screen """
        screen_rect = self.game_base.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
    
    def start_moving(self):
        self.moving = True

    def pause_moving(self):
        self.moving = False
