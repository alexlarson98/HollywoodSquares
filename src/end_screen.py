import pygame
import math
from player import Player
from text import Text

class EndScreen:
    def __init__(self, game_display, sizes):
        self.counter = 0
        self.game_display = game_display
        self.sizes = sizes
        self.surface = pygame.Surface((sizes.display_width, sizes.display_height))
        self.oswald_light_blue = (146,193,233)
        self.fade_finished = False

        self.winner = None
        self.winning_message = Text('', sizes.text_size*8,game_display,sizes.display_width/2,sizes.display_height-sizes.text_size*8)
        self.new_game_message = Text('PRESS ANY KEY TO START A NEW GAME!', 2*sizes.text_size, game_display, sizes.display_width/2, sizes.display_height-(2*sizes.text_size), blink=True)

        self.crown_width = math.ceil(sizes.display_width/5)
        self.crown_height = math.ceil(sizes.display_width/5)

        self.crown = pygame.image.load('./media/crown.png')
        self.crown = pygame.transform.scale(self.crown, (self.crown_width, self.crown_height))

        self.music = False
    
    def end_game(self):
        if not self.music:
            pygame.mixer.music.load("./media/sfx/hollywood_squares.mp3")
            pygame.mixer.music.play(loops=-1)
            self.music = True
        self.fade_out()
        if self.winner and self.fade_finished:
            self.display_winner()
        if not self.winner:
            raise Exception("Error: The game can't end without a winner!")

    def fade_out(self):
        if self.counter >= 256:
            self.fade_finished = True
        self.surface.set_alpha(self.counter)
        self.surface.fill(self.oswald_light_blue)
        self.game_display.blit(self.surface, (0,0))
        self.counter += 2

    def display_winner(self):
        self.game_display.blit(self.winner.player_img, (self.center_player_on_screen()))
        self.game_display.blit(self.crown, (self.put_crown_on()))
        self.winning_message.message_display()
        self.new_game_message.message_display()

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
        self.winning_message.change_text(winner.name + " wins!")
