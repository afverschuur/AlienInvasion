import sys
import pygame
from time import sleep

from settings import Settings
from soundfx import SoundFX
from gamestats import GameStats

from start_screen.start_screen import StartScreen
from play_game.play_game import PlayGame
from game_over.game_over import GameOver

# Alien Invasion
#
# Game has infinite Main While Loop within run_game in wich:
#
# 1 Inputs are handled (e.g. keyboard)
# 2 Assets are updated (e.g. ships move, aliens move etc..)
# 3 Screen is updated: redraw assets en flip screen (see pygame docs)
#
# For every Game Loop, see Classes.GameLoopInterface.
# 
# Every part of the game is defined as a different Game Loop: 
# 1 Start screen before playing
# 2 Playing the game
# 3 Game over
# 4 New Highscore: enter your name for Hall of Fame
#

class AlienInvasion:
    """ Class to manage game assets and behavior """

    def __init__(self):
        """ Init game and create assets """
        # Init pygame
        pygame.init()

        # Property to hold current Game loop
        self.current_loop = None
        
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

        # Load Game loop (parts of game run in the main loop of run_game)
        self.start_screen = StartScreen(self)
        self.play_game = PlayGame(self)
        self.game_over = GameOver(self)

        # Set initial Game loop
        self.switch_loop_to(self.start_screen)

    def run_game(self):
        """ Start the main loop for the game """
        # Start clock to set tempo
        clock = pygame.time.Clock()

        # Main loop
        while True:

            # Respond to inputs in current loop
            for event in pygame.event.get():
                self._check_events_all_loops(event)
                self.current_loop.check_events(event)
            # Update assets of current loop
            self.current_loop.update_assets()
            # Update screen of current loop
            self.current_loop.update_screen()

            # Make the last drawn screen visible
            pygame.display.flip()

            # Wait - implementing tempo
            clock.tick(200)

    def _check_events_all_loops(self, event):
        """ Responds to input during all loop """
        if event.type == pygame.KEYDOWN:
            # Key 'q' to exit game 
            if event.key == pygame.K_q:
                sys.exit()

    def switch_loop_to(self, loop):
        """ Changes Game loop """
        # Hook for event 'stop' of loop
        if self.current_loop:
            self.current_loop.stop()
        # Change loop
        self.current_loop = loop
        # Hook for event 'start' of loop
        self.current_loop.start()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
