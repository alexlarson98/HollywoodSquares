import pygame

class Grid:
    def __init__(self, sizes):
        self.sizes = sizes
        self.board = pygame.image.load('./media/hs_grid.png')
        self.board = pygame.transform.scale(self.board, (sizes.grid_size, sizes.grid_size))
        self.alt_board = None
        self.player_index = None
        self.count = 0

    def display_grid(self, game_display):
        if self.player_index is None:
            game_display.blit(self.board,((self.sizes.display_width-self.sizes.grid_size)*(self.sizes.grid_fraction),(self.sizes.display_height-self.sizes.grid_size)/2))
        else:
            if self.count > 15 and self.count <= 30:
                game_display.blit(self.alt_board,((self.sizes.display_width-self.sizes.grid_size)*(self.sizes.grid_fraction),(self.sizes.display_height-self.sizes.grid_size)/2))
            elif self.count <= 15:  
                game_display.blit(self.board,((self.sizes.display_width-self.sizes.grid_size)*(self.sizes.grid_fraction),(self.sizes.display_height-self.sizes.grid_size)/2))
            if self.count >=30:
                self.count = 0
            self.count += 1

    def set_player_index(self, index):
        self.alt_board = pygame.image.load(f'./media/hs_grid_{index}.png')
        self.alt_board = pygame.transform.scale(self.alt_board, (self.sizes.grid_size, self.sizes.grid_size))
        self.player_index = index

    def reset_player_index(self):
        self.alt_board = pygame.image.load('./media/hs_grid.png')
        self.alt_board = pygame.transform.scale(self.board, (self.sizes.grid_size, self.sizes.grid_size))