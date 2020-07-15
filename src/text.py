import pygame
import textwrap

class Text():
    def __init__(self, text, game_display, display_width, display_height,color=(0,0,0)):
        self.text = text
        self.font = pygame.font.SysFont('Comic Sans MS',24)
        self.surface = self.font.render(self.text, False, color)
        self.rectangle = self.surface.get_rect()
        self.color = color
        
        self.game_display = game_display
        self.display_width = display_width
        self.display_height = display_height

    def change_text(self, text):
        self.text = text
        self.surface = self.font.render(text, False, self.color)
        self.rectangle = self.surface.get_rect()

    def message_display(self):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        self.rectangle.center = (self.display_width, self.display_height)
        self.game_display.blit(self.surface, self.rectangle)
