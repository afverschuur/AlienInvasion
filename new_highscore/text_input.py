import pygame
import sys
from line import Line

class TextInput():
    """ Class to implement text input """

    def __init__(self) -> None:
        pygame.init()
        input = True

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.bg_color = (230,230,230)

        self.line = Line(self, 8)

    def start_input(self):
        while input:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.line.draw_line()
        pygame.display.flip()

    def _check_events(self):
        """ Respond to keyboard events """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_UP:
                    self.line.handle_input('UP')
                elif event.key == pygame.K_DOWN:
                    self.line.handle_input('DOWN')
                elif event.key == pygame.K_RIGHT:
                    self.line.handle_input('RIGHT')
                elif event.key == pygame.K_LEFT:
                    self.line.handle_input('LEFT')


if __name__ == '__main__':
    ti = TextInput()
    ti.start_input()