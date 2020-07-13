import pygame
import math

class Sizes():
    def __init__(self):
        info = pygame.display.Info()
        self.display_width = math.ceil((info.current_w*4)/5)
        self.display_height = math.ceil((info.current_h*4)/5)

        self.title_width = math.ceil((info.current_w * 3)/4)
        self.title_height = math.ceil((info.current_h * 3)/4)

        self.game_title_width = math.ceil((info.current_w * 3)/5)
        self.game_title_height = math.ceil((info.current_h)/8)

        self.grid_size = math.ceil((info.current_h * 1)/2)
        self.grid_fraction = (6/7)
        self.grid_increment = math.ceil(self.grid_size/3)

        self.start_button_width = math.ceil((info.current_w * 1)/10)
        self.start_button_height = math.ceil(self.start_button_width / 4)
        