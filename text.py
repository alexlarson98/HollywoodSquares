import pygame

class Text():
    def __init__(self, text):
        self.text = text
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.surface = self.font.render(self.text, False, (0, 0, 0))
        self.rectangle = self.surface.get_rect()

    def text_objects(self):
        textSurface = self.font.render(self.text, True, (0,0,0))
        return textSurface, textSurface.get_rect()

    def message_display(self, game_display, display_width, display_height):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        self.rectangle.center = ((display_width/2),(display_height/2))
        game_display.blit(self.surface, self.rectangle)
