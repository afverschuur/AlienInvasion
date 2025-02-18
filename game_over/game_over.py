from classes.game_status_interface import GameLoopInterface
from game_over.game_over_text import GameOverText
import pygame
from game_assets.ship import Ship 

class GameOver(GameLoopInterface):
    """ Class implementing start screen status """

    ######################################
    # INIT
    ######################################

    def __init__(self, game_base) -> None:
        super().__init__(game_base)
        self.textscreen = GameOverText(game_base, self.game_base.settings.bg_color, self.game_base.settings.init_pos_y)
        self.ship = Ship(game_base)

    ######################################
    # CHECK EVENTS
    ######################################

    def check_events(self, event) -> None:
        """ Responds to input """
        if event.type == pygame.KEYDOWN: 
            # Key 's' to start the game 
            if event.key == pygame.K_s:
                self.game_base.switch_loop_to(self.game_base.play_game)
                    

    ######################################
    # UPDATE ASSETS
    ######################################

    def update_assets(self) -> None:
        """ Update assets """
        pass

    ######################################
    # UPDATE SCREEN
    ######################################

    def update_screen(self) -> None:
        """ Redraw assets and flip the screen"""
        self.game_base.screen.fill(self.game_base.settings.bg_color)
        self.textscreen.draw()
        self.ship.blitme()

    ######################################
    # HOOKS
    ######################################

    def start(self) -> None:
        self.game_base.soundfx.music('music_start')