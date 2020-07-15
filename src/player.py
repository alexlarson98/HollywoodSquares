import pygame
import math

class Player:
    def __init__(self, img, name, sizes):
        self.player_img = pygame.image.load(img)
        self.width = math.ceil(sizes.display_width/5)
        self.height = math.ceil(sizes.display_width/4)
        self.player_img = pygame.transform.scale(self.player_img, (self.width, self.height))
        self.name = name
        self.letter = self.name[-1]

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_letter(self):
        return self.letter

    def get_opposite_letter(self):
        if self.letter == "X":
            return "O"
        return "X"