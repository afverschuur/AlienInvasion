import pygame.font

class Highscore:
    """ Class representing scoreboard """

    def __init__(self, ai_game) -> None:
        """ Init """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.images = []

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_title()
        self.prep_top(1, "Fred", 1000000)
        self.prep_top(2, "Tijmen", 800000)
        self.prep_top(3, "Florian", 700000)

    def prep_title(self):
        """ Turn topscore in rendered image """
        score_img = self.font.render("HIGHSCORE", True, self.text_color, self.settings.bg_color)

        # Display score 
        score_rect = score_img.get_rect()
        score_rect.center = self.screen_rect.center
        score_rect.top = 100 
        self.images.append((score_img, score_rect))

    def prep_top(self, place, name, score):
        """ Turn topscore in rendered image """
        name_str = str(name).ljust(8)
        score_str = str(score).rjust(10, "0")
        score_str = f"{place}. {name_str} {score}"
        score_img = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display score 
        score_rect = score_img.get_rect()
        score_rect.center = self.screen_rect.center
        score_rect.top = 100 + place * 50

        self.images.append((score_img, score_rect))

    def draw_highscore(self):
        """ Draw highscores to screen """
        for img, rect in self.images:
            self.screen.blit(img, rect)