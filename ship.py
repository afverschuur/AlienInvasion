import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ Class representing a ship """

    def __init__(self, ai_game) -> None:
        """ Init ship and set starting position """
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # New ship
        self.new_ship()
        self.exploding = False
        self.exploding_frames = 0

    def new_ship(self):
        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.exploding = False
        self.exploding_frames = 0
        
        # Start at bottom center
        self.center_ship()

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """ Update position based on movement flags """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Move ship to the right
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            # Move ship to the left
            self.x -= self.settings.ship_speed
        
        # Update ship's rect from self.x
        self.rect.x = self.x

        # Exploding
        if self.exploding:
            self.exploding_frames += 1
            if self.exploding_frames == 50:
                self.new_ship()

    def blitme(self):
        """ Draw ship at current position """
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def explode(self):

        self.image = pygame.image.load('images/ship_exploded.png').convert_alpha()
        #self.rect = self.image.get_rect()
        self.exploding = True

