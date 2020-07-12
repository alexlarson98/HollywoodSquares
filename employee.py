import pygame

class Emmployee():
    def __init__(self, name, order, x_or_o=None):
        self.name = name
        self.order = order
        self.x_or_o = x_or_o
        self.is_available = True
        self.rectangle = None

    def is_available(self):
        return self.is_available

    def set_rectangle(self, x, y, box_size):
        self.rectangle = pygame.Rect(x, y, box_size, box_size)