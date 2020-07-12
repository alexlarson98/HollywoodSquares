import pygame

class Text():
    def __init__(self, text, game_display, display_width, display_height):
        self.text = text
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.surface = self.font.render(self.text, False, (0, 0, 0))
        self.rectangle = self.surface.get_rect()
        self.game_display = game_display
        self.display_width = display_width
        self.display_height = display_height

    def message_display(self):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        self.rectangle.center = (self.display_width, self.display_height)
        self.game_display.blit(self.surface, self.rectangle)
