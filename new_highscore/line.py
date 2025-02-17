import pygame
from pygame.font import Font

class Line:
    def __init__(self, text_input, length) -> None:
        self.screen = text_input.screen
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.Font("./font/SpaceMono-Regular.ttf", 32) 
        self.text_color = (0, 0, 0)
        self.bg_color = text_input.bg_color
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
        self.image = self.font.render(''.join(self.input), True, self.text_color, self.bg_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center
        self.image_rect.top = 400

    def draw_line(self):
        self.screen.blit(self.image, self.image_rect)

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
