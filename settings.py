class Settings:
    """ Class with all settings for Alien Invasion """

    def __init__(self):
        # Screen settings
        self.screen_width = 1150
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_limit = 3
        self.ship_sound_fire = "sounds/laser.mp3"

        # Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10
        self.alien_sound_explosion = "sounds/explosion.mp3"

        # Game
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.game_sound_gameover = "sounds/gameover.mp3"
        self.game_sound_music = "sounds/music1.mp3"
        self.game_sound_levelup = "sounds/levelup2.mp3"
        self.game_sound_start = "sounds/countdown.mp3"

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


        

    