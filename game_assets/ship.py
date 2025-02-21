import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ Class representing a ship """

    def __init__(self, game_base) -> None:
        """ Init ship and set starting position """
        super().__init__()
        self.game_base = game_base
        
        # New ship
        self.new_ship()

    def new_ship(self):
        """ Create new ship """
        # Load ship image and get its rect
        self.image = pygame.image.load('assets/images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start at bottom center
        self.center_ship()

        # Flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """ Update position based on movement flags, handle explosion """
        if self.moving_right and self.rect.right < self.game_base.screen_rect.right:
            # Move ship to the right
            self.x += self.game_base.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            # Move ship to the left
            self.x -= self.game_base.settings.ship_speed
        
        # Update ship's rect from self.x
        self.rect.x = self.x

    def blitme(self):
        """ Draw ship at current position """
        self.game_base.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """ Center ship """
        self.rect.midbottom = self.game_base.screen_rect.midbottom
        self.x = float(self.rect.x)


