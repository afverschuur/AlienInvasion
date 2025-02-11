import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Class representing bullet fired from a ship """

    def __init__(self, ai_game):
        """ Create bullet at ships position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet and set to correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet's position
        self.y = float(self.rect.y)

    def update(self):
        """ Move bullet up the screen """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw bullet to screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
