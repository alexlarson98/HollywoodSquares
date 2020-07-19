import pygame
import math

class Sizes():
    def __init__(self):
        info = pygame.display.Info()
        self.display_width = math.ceil(info.current_w * (6/7))
        self.display_height = math.ceil(info.current_h * (6/7))

        self.text_size = math.ceil((self.display_height*2)/100)

        self.title_width = math.ceil((self.display_width * 6)/7)
        self.title_height = math.ceil((self.display_height * 6)/7)

        self.game_title_width = math.ceil((self.display_width * 6)/7)
        self.game_title_height = math.ceil((self.display_height)/7)

        self.grid_size = math.ceil((self.display_height * 2)/3)
        self.grid_fraction = (6/7)
        self.grid_increment = math.ceil(self.grid_size/3)

        self.start_button_width = math.ceil((self.display_width)/6)
        self.start_button_height = math.ceil(self.start_button_width / 3)

        self.buffer_width = math.ceil(self.display_width / 100)
        
        