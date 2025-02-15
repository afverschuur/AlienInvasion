import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """ Init """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.button_width, self.button_height = 200, 50
        self.button_color = (0, 255, 0)
        self.button_text_color = (255, 255, 255)
        self.button_font = pygame.font.Font(self.settings.font, 32) 

        self.update_pos()
        self._prep_msg(msg)

    def update_pos(self):
        pass

    def _prep_button(self, msg):
        """ Turn msg into rendered image """
        self.button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.button_rect.center = self.screen_rect.center
        self.settings.start_pos += 70
        self.button_rect.top = self.settings.start_pos
        self.msg_image = self.font.render(msg, True, self.button_text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.top = self.button_rect.top

    def draw_button(self):
        """ Draw button and message """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
