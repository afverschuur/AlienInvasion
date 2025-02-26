import pygame

pygame.init()

#initialise the joystick module
pygame.joystick.init()

#create game window
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
SCREEN_WIDTH = screen.get_rect().width
SCREEN_HEIGHT = screen.get_rect().height

pygame.display.set_caption("Joysticks")

#define font
font_size = 30
font = pygame.font.SysFont("Futura", font_size)

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#create clock for setting game frame rate
clock = pygame.time.Clock()
FPS = 60

#create empty list to store joysticks
joysticks = []

#create player rectangle
x = (SCREEN_WIDTH-100)/2
y = (SCREEN_HEIGHT-100)/2
player = pygame.Rect(x, y, 100, 100)

#define player colour
col = "royalblue"

#game loop
run = True
while run:

    clock.tick(FPS)

    #update background
    screen.fill(pygame.Color("midnightblue"))

    #draw player
    player.topleft = (x, y)
    pygame.draw.rect(screen, pygame.Color(col), player)

    #show number of connected joysticks
    draw_text("Controllers: " + str(pygame.joystick.get_count()), font, pygame.Color("azure"), 10, 10)
    for joystick in joysticks:
        draw_text("Battery Level: " + str(joystick.get_power_level()), font, pygame.Color("azure"), 10, 35)
        draw_text("Controller Type: " + str(joystick.get_name()), font, pygame.Color("azure"), 10, 60)
        draw_text("Number of axes: " + str(joystick.get_numaxes()), font, pygame.Color("azure"), 10, 85)
    
    draw_text("Screen resolution: ", font, pygame.Color("azure"), 10, 130)
    draw_text("Width: " + str(SCREEN_WIDTH), font, pygame.Color("azure"), 10, 160)
    draw_text("Height: " + str(SCREEN_HEIGHT), font, pygame.Color("azure"), 10, 190)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
        #quit program
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False

    for joystick in joysticks:
        #change player colour with buttons
        if joystick.get_button(0):
            col = "royalblue"
        if joystick.get_button(1):
            col = "crimson"
        if joystick.get_button(2):
            col = "fuchsia"
        if joystick.get_button(3):
            col = "forestgreen"

        if joystick.get_button(14):
            x += 5
        if joystick.get_button(13):
            x -= 5
        if joystick.get_button(11):
            y -= 5
        if joystick.get_button(12):
            y += 5

        #player movement with analogue sticks
        horiz_move = joystick.get_axis(0)
        vert_move = joystick.get_axis(1)
        if abs(vert_move) > 0.05:
            y += vert_move * 5
        if abs(horiz_move) > 0.05:
            x += horiz_move * 5

    #update display
    pygame.display.flip()

pygame.quit()

