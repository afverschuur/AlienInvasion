class Settings:
    """ Class with all settings """

    def __init__(self):

        # Game
        self.title = "Alien Invasion"

        # Screen settings
        self.bg_color = (230,230,230)
        self.screen_height = 1100   # overwritten in case of fullscreen
        self.screen_width = 800     # overwritten in case of fullscreen
        self.init_pos_y = self.screen_height / 6

        # Ship settings
        self.ship_limit = 1

        # Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Gameplay
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # Set fonts
        self.font = "assets/fonts/SpaceMono-Regular.ttf"
        self.font_title = "assets/fonts/Monofett-Regular.ttf"
        self.font_color = (30, 30, 30)

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1.0
        # 1 = right, -1 = left
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """ Increase speed settings """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


        

    