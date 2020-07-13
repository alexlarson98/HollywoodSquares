import pygame
import math
from button import Button
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
# pygame.mixer.music.play(loops=-1)

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

# Button initializations
correct_button = Button(green, 50, sizes.display_height-150, 250, 100, 'CORRECT')
incorrect_button = Button(red, sizes.display_width-300, sizes.display_height-150, 250, 100, 'INCORRECT')

# Set up the drawing window
game_display = pygame.display.set_mode((sizes.display_width,sizes.display_height))
pygame.display.set_caption('The Oswald Squares')

# Setup game object
game = Game(game_display, sizes)

# Text initializations
start_screen_message = Text('Press any key to continue!', game_display, sizes.display_width/2, sizes.display_height-30)

# Image manipulation
start_title = pygame.image.load('./media/hollywood_title.png')
start_title = pygame.transform.scale(start_title, (sizes.title_width,sizes.title_height))

game_title = pygame.image.load('./media/hollywood_title_horizontal.png')
game_title = pygame.transform.scale(game_title, (sizes.game_title_width,sizes.game_title_height))

grid = pygame.image.load('./media/hs_grid.png')
grid = pygame.transform.scale(grid, (sizes.grid_size, sizes.grid_size))

pygame.display.set_icon(grid) # Change Icon!

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

######################################## START GAME ############################################
# Run game until the user asks to quit
while running:

    for event in  pygame.event.get():
        # Mouse position
        pos = pygame.mouse.get_pos()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Check employee grid
                game.in_square(pos)
                # Check if the game is being started
                game.start(pos)

        elif event.type == pygame.MOUSEMOTION:
            if correct_button.isOver(pos):
                correct_button.color = dark_green
            else:
                correct_button.color = green
            if incorrect_button.isOver(pos):
                incorrect_button.color = dark_red
            else:
                incorrect_button.color = red

        elif event.type == pygame.QUIT:
            running = False

    # Start screen background and text
    game_display.fill(oswald_light_blue)
    game_display.blit(game_title,((sizes.display_width-sizes.game_title_width)/2,0))

    # Display host
    game.display_host()

    # If there's an active game
    if game.is_active():
        # correct_button.draw(game_display)
        # incorrect_button.draw(game_display)
        
        if game.game_state == 2:
            game.choose_contestant()
    else:
        game.display_start_button()
    
    # Always show the board
    game.draw_squares(game_display)

    # Display messages
    game.display_all_messages()

    # Display grid
    game_display.blit(grid,((sizes.display_width-sizes.grid_size)*(sizes.grid_fraction),(sizes.display_height-sizes.grid_size)/2))

    # Flip the display
    pygame.display.flip()

################################################################################################

pygame.quit()
