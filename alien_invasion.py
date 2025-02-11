import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Class to manage game assets and behavior """

    def __init__(self):
        """ Init game and create assets """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """ Respond to keyboard or mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    
    def _update_screen(self):
        """ Redraw screen and flip to nwe screen """
        # Redraw screen 
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the last drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
