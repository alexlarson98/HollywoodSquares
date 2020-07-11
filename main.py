import pygame
import math
from button import Button
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

# Import and initialize the pygame library
pygame.init()

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Play loading music
pygame.mixer.music.load("./media/hollywood_squares.mp3")
# pygame.mixer.music.play(loops=-1)

# Set constants
info = pygame.display.Info()
display_width = math.ceil((info.current_w*4)/5)
display_height = math.ceil((info.current_h*4)/5)
title_width = math.ceil((info.current_w * 1)/2)
title_height = math.ceil((info.current_h * 1)/2)
grid_size = title_height

# Setup game object
game = Game(display_width, display_height, grid_size)

# Colors
black = (0,0,0)
green = (0,128,0)
dark_green = (0,75,0)
red = (255,0,0)
dark_red = (128,0,0)
white = (255,255,255)
oswald_light_blue = (146,193,233)

# Button initializations
correct_button = Button(green, 50, display_height-150, 250, 100, 'CORRECT')
incorrect_button = Button(red, display_width-300, display_height-150, 250, 100, 'INCORRECT')

# Set up the drawing window
game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Oswald Squares')
# pygame.display.set_icon(grid)

# Image manipulation
picture = pygame.image.load('./media/hollywood_title.png')
picture = pygame.transform.scale(picture, (title_width,title_height))
grid = pygame.image.load('./media/grid.jpg')
grid = pygame.transform.scale(grid, (grid_size,grid_size))

# Run start screen until the user asks to quit or start
starting = True
running = False
while starting:
    # Did the user click the window close button?
    for event in  pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            starting = False
            running = True

    # Start screen background and text
    game_display.fill(oswald_light_blue)
    game_display.blit(picture,((display_width-title_width)/2,(display_height-title_height)/2))

    # Flip the display
    pygame.display.flip()

# Run game until the user asks to quit
while running:

    # Did the user click the window close button?
    for event in  pygame.event.get():
        # Mouse position
        pos = pygame.mouse.get_pos()

        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.in_square(pos)
                

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

    # If there's an active game
    if not game.is_active():
        correct_button.draw(game_display)
        incorrect_button.draw(game_display)
        game.draw_squares(game_display)

    # Display grid
    game_display.blit(grid,((display_width-grid_size)/2,(display_height-grid_size)/2))

    # Flip the display
    pygame.display.flip()

pygame.quit()

def main():
    print('Hello, game!')

main()