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

        # Highscore
        self.images = []

        # Font settings
        self.text_color = (30, 30, 30)
        self.text_color_gametitle = (8, 168, 37)
        self.font = pygame.font.Font(self.settings.font, 28)
        self.font_big = pygame.font.Font(self.settings.font, 42)
        self.font_gametitle = pygame.font.Font(self.settings.font_gametitle, 70)

        self.update()

    def update(self):
        self.images.clear()
        if self.stats.game_over:
            self._prep_gameover()
        self._prep_gametitle()
        self._prep_title()
        for place, (name, highscore) in enumerate(self.stats.highscores):
            self._prep_highscore(place+1, name, highscore)
        self._prep_play()
    
    def _prep_gameover(self):
        """ Turn GAME OVER in rendered image """
        self.settings.start_pos -= 60
        text_img = self.font_big.render("GAME OVER!", True, self.text_color, self.settings.bg_color)

        # Display text 
        text_rect = text_img.get_rect()
        text_rect.center = self.screen_rect.center
        text_rect.top = self.settings.start_pos
        self.images.append((text_img, text_rect))
        self.settings.start_pos += 80

    def _prep_gametitle(self):
        """ Turn topscore in rendered image """
        score_img = self.font_gametitle.render("Alien Invasion", True, self.text_color_gametitle, self.settings.bg_color)

        # Display score 
        score_rect = score_img.get_rect()
        score_rect.center = self.screen_rect.center
        score_rect.top = self.settings.start_pos
        self.images.append((score_img, score_rect))
        self.settings.start_pos += 100 

    def _prep_title(self):
        """ Turn topscore in rendered image """
        score_img = self.font.render("HIGHSCORE", True, self.text_color, self.settings.bg_color)

        # Display score 
        score_rect = score_img.get_rect()
        score_rect.center = self.screen_rect.center
        score_rect.top = self.settings.start_pos
        self.images.append((score_img, score_rect))
        self.settings.start_pos += 50

    def _prep_highscore(self, place, name, score):
        """ Turn topscore in rendered image """
        name_str = str(name).ljust(8)
        score_str = "{:,}".format(score).rjust(10, " ")
        score_str = f"{place}. {name_str} {score_str}"
        score_img = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display score 
        score_rect = score_img.get_rect()
        score_rect.center = self.screen_rect.center
        score_rect.top = self.settings.start_pos

        self.images.append((score_img, score_rect))
        self.settings.start_pos += 50

    def _prep_play(self):
        """ Turn play in rendered image """
        self.settings.start_pos += 70
        score_img = self.font.render("Press 'up' to play", True, self.text_color, self.settings.bg_color)

        # Display score 
        score_rect = score_img.get_rect()
        score_rect.center = self.screen_rect.center
        score_rect.top = self.settings.start_pos
        self.images.append((score_img, score_rect))
        self.settings.start_pos += 50

    def draw_highscore(self):
        """ Draw highscores to screen """
        for img, rect in self.images:
            self.screen.blit(img, rect)
        self.settings.start_pos = self.settings.init_pos