import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Class representing bullet fired from a ship """

    def __init__(self, game_base):
        """ Create bullet at ships position """
        super().__init__()
        self.game_base = game_base
        self.color = self.game_base.settings.bullet_color

        # Create bullet and set to correct position
        self.rect = pygame.Rect(0, 0, self.game_base.settings.bullet_width, self.game_base.settings.bullet_height)
        self.rect.midtop = self.game_base.play_game.ship.rect.midtop

        # Store bullet's position
        self.y = float(self.rect.y)

    def update(self):
        """ Move bullet up the screen """
        self.y -= self.game_base.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw bullet to screen """
        pygame.draw.rect(self.game_base.screen, self.color, self.rect)
