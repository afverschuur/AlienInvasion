# Informal Interface
#
# Alien Invasion has a infinite Main While Loop in which:
# 1 Inputs are handled (e.g. keyboard)
# 2 Assets are updated (e.g. ships move, aliens move etc..)
# 3 Screen is updated: redraw assets en flip screen (see pygame docs)
# 
# Every part of the game is defined as an Game Loop: 
# 1 Start screen before playing
# 2 Playing the game
# 3 Game over
# 4 New Highscore: enter your name for Hall of Fame
#
# To implement a Game Loop use this interface.
#
# Constructor: Feed the game base-class to give a Game Loop access to the sceen, settings and stats 

class GameLoopInterface:
    """ Informal interface for implementing a Game Loop"""

    def __init__(self, game_base) -> None:
        # For access to screen, settings and stats
        self.game_base = game_base

    def check_events(self, event) -> None:
        """ Responds to input """ 
        pass

    def update_assets(self) -> None:
        """ Update assets """
        pass

    def update_screen(self) -> None:
        """ Redraw assets and flip the screen"""
        pass

    def stop(self) -> None:
        """ Hook for event 'stop' of status """
        pass
        
    def start(self) -> None:
        """ Hook for event 'start' of status """
        pass

