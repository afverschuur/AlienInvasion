import pygame
from pygame.font import Font

class InputLine:
    def __init__(self, game_base, length) -> None:
        self.game_base = game_base
        self.font = pygame.font.Font(self.game_base.settings.font, 32) 
        
        self.input = []
        self.charstring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
        self.chars = list(self.charstring)
        self.selected_place = 0
        self.selected_char = 0

        for i in range(length):
            self.input.append('_')
        self._prep_img()

    def _prep_img(self):
        self._update_selected()
        self.image = self.font.render(''.join(self.input), True, self.game_base.settings.font_color, self.game_base.settings.bg_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.game_base.screen_rect.center

    def draw(self, pos_y):
        self.image_rect.top = pos_y
        self.game_base.screen.blit(self.image, self.image_rect)

    def _update_selected(self):
        self.input[self.selected_place] = self.chars[self.selected_char % 27]

    def handle_input(self, key):
        match key:
            case 'UP':
                self.selected_char += 1
                self._update_selected()
            case 'DOWN':
                self.selected_char -= 1
                self._update_selected()
            case 'RIGHT':
                if self.selected_place < len(self.input) - 1:
                    self.selected_place += 1
                    self.selected_char = 0
                    self._update_selected()
            case 'LEFT':
                if self.selected_place > 0:
                    self.input[self.selected_place] = '_'
                    self.selected_place -= 1
                    char = self.input[self.selected_place]
                    index = self.charstring.find(str(char))
                    self.selected_char = index
                    self.input[self.selected_place] = '_'
        
        self._prep_img()

    def get_input(self):
        joined_input = ''.join(self.input)
        cleaned_input = joined_input.rstrip('_ ')
        return cleaned_input
