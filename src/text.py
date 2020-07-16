import pygame
import textwrap

class Text():
    def __init__(self,text,text_size,game_display, display_width, display_height,color=(0,0,0),blink=False):
        self.text = text
        self.font = pygame.font.SysFont('Comic Sans MS',text_size)
        self.surface = self.font.render(self.text, False, color)
        self.rectangle = self.surface.get_rect()
        self.color = color
        
        self.game_display = game_display
        self.display_width = display_width
        self.display_height = display_height

        self.blink = blink
        self.blink_count = 0

    def change_text(self, text):
        self.text = text
        self.surface = self.font.render(text, False, self.color)
        self.rectangle = self.surface.get_rect()

    def message_display(self):
        if self.blink:
            if self.blink_count <= 40:
                self.rectangle.center = (self.display_width, self.display_height)
                self.game_display.blit(self.surface, self.rectangle)
            if self.blink_count >= 80:
                self.blink_count = 0
            self.blink_count += 1
        else:
            self.rectangle.center = (self.display_width, self.display_height)
            self.game_display.blit(self.surface, self.rectangle)

