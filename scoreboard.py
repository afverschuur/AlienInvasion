import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """ Class representing scoreboard """

    def __init__(self, ai_game) -> None:
        """ Init """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """ Turn score in rendered image """
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display score at top right
        self.score_rect = self.score_img.get_rect()
        self.score_rect.center = self.screen_rect.center
        self.score_rect.top = 20

    def prep_level(self):
        """ Turn level in rendered image """
        level_str = str(self.stats.level)
        self.level_img = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Display level below score
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 20

    def prep_ships(self):
        """ Show how many ships left """
        self.ships = Group()
        for ship_nr in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_nr * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def draw_score(self):
        """ Draw score to screen """
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)