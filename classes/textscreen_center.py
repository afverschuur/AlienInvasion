# Class to build a centertextscreen, extend for your own textscreen
#
# Pygame needs all text to render as images before drawing to screen. The methods of this class
# take care of this. All text will be centered. 
#
# Constructor: Feed the game base-class to give a Screen access to the screen, settings and stats 

class TextScreenCenter:
    """ Class to build a screen """
    def __init__(self, game_base, bg_color, start_pos_y) -> None:
        # For access to screen, settings and stats
        self.game_base = game_base
        # Backgroundcolor of screen
        self.bg_color = bg_color
        # Start position on y-axis
        self.init_pos_y = start_pos_y
        # Cursor on y-axis, marks point where to draw
        self.cursor_pos_y = start_pos_y

        # Collecion of the images to draw
        self.images = []

        # Feed text, pygame Font and RGB color (R, G, B) 
    def render_text(self, text, font, color) -> None:
        """ Render text to image and add to images to draw """
        # Render text to image
        img = font.render(text, True, color, self.bg_color)

        # Figure out rectangle
        rect = img.get_rect()
        # Center in screen
        rect.center = self.game_base.screen_rect.center
        # Set position on y-axis of screen
        rect.top = self.cursor_pos_y
        # Add to images to draw
        self.images.append((img, rect))
        # Move y-cursor with height of rectangle of rendered image
        self.cursor_pos_y += rect.height

    def add_whitespace(self, size) -> None:
        """ Add vertical whitespace """
        self.cursor_pos_y += size

    def draw(self) -> None:
        """ Draw images to the gamescreen """
        for img, rect in self.images:
            self.game_base.screen.blit(img, rect)
        # Reset cursor
        self.cursor_pos_y = self.init_pos_y

    # Implement own update method to update screen
    def update(self) -> None:
        pass

    