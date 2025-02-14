class GameStats:
    """ Track statistics for Alien Invasion """

    def __init__(self, ai_game):
        """ Init """
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.game_over = False
    
    def reset_stats(self):
        """ Init stats """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.game_over = False