import pygame.font
from pygame.sprite import Group
from game_assets.ship import Ship

class Scoreboard:
    """ Class representing scoreboard """

    def __init__(self, game_base) -> None:
        """ Init """
        self.game_base = game_base

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font(self.game_base.settings.font, 32)
        self.topmargin = 10

        self.update()

    def update(self):
        """ Update scoreboard """
        self._prep_score()
        self._prep_level()
        self._prep_ships()

    def _prep_score(self):
        """ Turn score in rendered image """
        rounded_score = round(self.game_base.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str, True, self.text_color, self.game_base.settings.bg_color)

        # Display score at top right
        self.score_rect = self.score_img.get_rect()
        self.score_rect.center = self.game_base.screen_rect.center
        self.score_rect.top = self.topmargin

    def _prep_level(self):
        """ Turn level in rendered image """
        level_str = f"Level: {self.game_base.stats.level}"
        self.level_img = self.font.render(level_str, True, self.text_color, self.game_base.settings.bg_color)

        # Display level below score
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.game_base.screen_rect.right - self.level_rect.width - 10
        self.level_rect.top = self.topmargin

    def _prep_ships(self):
        """ Show how many ships left """
        self.ships = Group()
        for ship_nr in range(self.game_base.stats.ships_left-1):
            ship = Ship(self.game_base)
            ship.rect.x = 10 + ship_nr * ship.rect.width
            ship.rect.y = self.topmargin
            self.ships.add(ship)

    def draw(self):
        """ Draw scoreboard to screen """
        self.game_base.screen.blit(self.score_img, self.score_rect)
        self.game_base.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.game_base.screen)