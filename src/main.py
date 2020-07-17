import pygame
import math
from button import Button
from end_screen import EndScreen
from sizes import Sizes
from text import Text
from game import Game

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Setup for sounds. Defaults are good.
pygame.mixer.init()

# Setup for text and font
pygame.font.init()

# Import and initialize the pygame library
pygame.init()

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Play loading music
pygame.mixer.music.load("./media/hollywood_squares.mp3")
pygame.mixer.music.play(loops=-1)

# Set constants
sizes = Sizes()

# Colors
black = (0,0,0)
green = (0,128,0)
dark_green = (0,75,0)
red = (255,0,0)
dark_red = (128,0,0)
white = (255,255,255)
oswald_light_blue = (146,193,233)

# Starting player index
first_player = 0

# Set up the drawing window
game_display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('The Oswald Squares')

# Setup game object
game = Game(game_display, sizes, first_player)

# Setup end screen
end_screen = EndScreen(game_display, sizes)

# Text initializations
start_screen_message = Text('PRESS ANY KEY TO START!', 2*sizes.text_size, game_display, sizes.display_width/2, sizes.display_height-(2*sizes.text_size), blink=True)

# Image manipulation
start_title = pygame.image.load('./media/hollywood_title.png')
start_title = pygame.transform.scale(start_title, (sizes.title_width,sizes.title_height))

game_title = pygame.image.load('./media/hollywood_title_horizontal.png')
game_title = pygame.transform.scale(game_title, (sizes.game_title_width,sizes.game_title_height))

# pygame.display.set_icon(grid) # Change Icon!

###################################### START SCREEN ############################################

# Run start screen until the user asks to quit or start
starting = True
running = False
while starting:
    # Did the user click the window close button?
    for event in  pygame.event.get():
        if event.type == KEYDOWN:
            starting = False
            running = True

    # Start screen background and text
    game_display.fill(oswald_light_blue)
    game_display.blit(start_title,((sizes.display_width-sizes.title_width)/2,(sizes.display_height-sizes.title_height)/2))

    # Display text at start screen
    start_screen_message.message_display()

    # Flip the display
    pygame.display.flip()

game.start()
pygame.mixer.music.fadeout(4000)

######################################## START GAME ############################################
# Run game until the user asks to quit
while running:

    for event in  pygame.event.get():
        # Mouse position
        pos = pygame.mouse.get_pos()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif game.game_state == 6:
                if not first_player:
                    first_player = 1
                else:
                    first_player = 0
                game = Game(game_display, sizes, first_player)
                game.start()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Check employee grid
                game.in_square(pos)
                # Check buttons
                game.in_button(pos)

        elif event.type == pygame.MOUSEMOTION:
            game.button_hover_check(pos)

        elif event.type == pygame.QUIT:
            running = False

    # Start screen background and text
    game_display.fill(oswald_light_blue)
    game_display.blit(game_title,((sizes.display_width-sizes.game_title_width)/2,0))

    # Display host
    game.display_host()

    # If there's an active game
    if game.is_active():
        if game.game_state == 2:
            game.choose_celebrity()
        if game.game_state == 3:
            game.ask_question()
            game.display_buttons()
        if game.game_state == 4:
            game.mark_grid()
        if game.game_state == 5:
            game.check_winner()
    
    # Always show the board
    game.draw_squares(game_display)

    # Display messages
    game.display_all_messages()

    # Display Board
    game.display_board()

    # Display all X's and O's
    game.draw_x_and_o()

    if game.game_state == 6:
        game.end()

    # Flip the display
    pygame.display.flip()

################################################################################################

pygame.quit()
