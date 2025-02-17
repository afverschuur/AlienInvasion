import sys
import pygame
from time import sleep

from settings import Settings
from soundfx import SoundFX
from gamestats import GameStats

from start_screen.start_screen import StartScreen
from play_game.play_game import PlayGame
from game_over.game_over import GameOver

class AlienInvasion:
    """ Class to manage game assets and behavior """

    def __init__(self):
        """ Init game and create assets """
        # Init pygame
        pygame.init()

        # Property to hold current Game Status
        self.current_status = None
        
        # Load settings
        self.settings = Settings()

        # Load gamestats 
        self.stats = GameStats(self)

        # Display: Fullscreen 
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # Figure out rectangle of screen (needed in other classes, eg CenterTextScreen)
        self.screen_rect = self.screen.get_rect()
        # Update settings
        self.settings.screen_width = self.screen_rect.width
        self.settings.screen_height = self.screen_rect.height

        # Set caption
        pygame.display.set_caption(self.settings.title)
        # Hide mousepointer
        pygame.mouse.set_visible(False)

        # Init soundeffects
        self.soundfx = SoundFX()

        # Load Game Status (parts of game run in the main loop of run_game)
        self.start_screen = StartScreen(self)
        self.play_game = PlayGame(self)
        self.game_over = GameOver(self)

        # Set initial Game Status
        self.change_status_to(self.start_screen)

    def run_game(self):
        """ Start the main loop for the game """
        # Start clock to set tempo
        clock = pygame.time.Clock()

        # Main loop
        while True:

            # Respond to inputs in current status
            for event in pygame.event.get():
                self._check_events_all_status(event)
                self.current_status.check_events(event)
            # Update assets of current status
            self.current_status.update_assets()
            # Update screen of current status
            self.current_status.update_screen()

            # Make the last drawn screen visible
            pygame.display.flip()

            # Wait - implementing tempo
            clock.tick(200)

    def _check_events_all_status(self, event):
        """ Responds to input during all status """
        if event.type == pygame.KEYDOWN:
            # Key 'q' to exit game 
            if event.key == pygame.K_q:
                sys.exit()

    def change_status_to(self, status):
        """ Changes Game Status """
        # Hook for event 'stop' of status
        if self.current_status:
            self.current_status.stop()
        # Change status
        self.current_status = status
        # Hook for event 'start' of status
        self.current_status.start()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
