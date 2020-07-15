import pygame
import math
from player import Player

class EndScreen:
    def __init__(self, game_display, sizes):
        self.counter = 0
        self.game_display = game_display
        self.sizes = sizes
        self.surface = pygame.Surface((sizes.display_width, sizes.display_height))
        self.oswald_light_blue = (146,193,233)
        self.fade_finished = False
        self.winner = None

        self.crown_width = math.ceil(sizes.display_width/5)
        self.crown_height = math.ceil(sizes.display_width/5)

        self.crown = pygame.image.load('./media/crown.png')
        self.crown = pygame.transform.scale(self.crown, (self.crown_width, self.crown_height))
    
    def end_game(self):
        # if not self.fade_finished:
        self.fade_out()
        # else:
        if self.winner and self.fade_finished:
            self.display_winner()
        if not self.winner:
            raise Exception("Error: The game can't end without a winner!")

    def fade_out(self):
        if self.counter >= 256:
            # self.counter = 0
            self.fade_finished = True
        # else:
        self.surface.set_alpha(self.counter)
        self.surface.fill(self.oswald_light_blue)
        self.game_display.blit(self.surface, (0,0))
        self.counter += 2

    def display_winner(self):
        self.game_display.blit(self.winner.player_img, (self.center_player_on_screen()))
        self.game_display.blit(self.crown, (self.put_crown_on()))

    def center_player_on_screen(self):
        width = math.ceil((self.sizes.display_width-self.winner.width)/2)
        height = math.ceil(((self.sizes.display_height-self.winner.height) * 2 )/3)
        return (width, height)

    def put_crown_on(self):
        player_width, player_height = self.center_player_on_screen()
        height = math.ceil(player_height-self.crown_height)
        return (player_width, height)

    def set_winner(self, winner):
        self.winner = winner
