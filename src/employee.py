import pygame

class Emmployee():
    def __init__(self, name, order, x_or_o=None):
        self.name = name
        self.order = order
        self.x_or_o = x_or_o
        self.available = True
        self.rectangle = None
        self.shape = None

    def is_available(self):
        return self.available

    def draw(self, game_display):
        if not self.x_or_o:
            raise Exception('Error: x/o is null')
        game_display.blit(self.shape, (self.rectangle.x, self.rectangle.y))

    def set_shape(self, img_url):
        self.shape = pygame.image.load(img_url)
        self.shape = pygame.transform.scale(self.shape, (self.rectangle.width,self.rectangle.height))

    def set_not_available(self):
        self.available = False

    def set_rectangle(self, x, y, box_size):
        self.rectangle = pygame.Rect(x, y, box_size, box_size)

    def set_x_or_o(self, x_or_o):
        self.x_or_o = x_or_o

    def get_x_or_o(self):
        return self.x_or_o