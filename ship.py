import pygame

class Ship:
    """ Class representing a ship """

    def __init__(self, ai_game) -> None:
        """ Init ship and set starting position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
    
    def update(self):
        """ Update position based on movement flags """
        if self.moving_right:
            # Move ship to the right
            self.rect.x += 1

    def blitme(self):
        """ Draw ship at current position """
        self.screen.blit(self.image, self.rect)

