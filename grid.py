import pygame

class Grid:
    def __init__(self, sizes):
        self.sizes = sizes
        self.board = pygame.image.load('./media/hs_grid.png')
        self.board = pygame.transform.scale(self.board, (sizes.grid_size, sizes.grid_size))

    def display_grid(self, game_display):   
        game_display.blit(self.board,((self.sizes.display_width-self.sizes.grid_size)*(self.sizes.grid_fraction),(self.sizes.display_height-self.sizes.grid_size)/2))