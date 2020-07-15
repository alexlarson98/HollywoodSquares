import pygame
import math

HOST_STOP_LEFT = 0
HOST_STOP_RIGHT = 1
HOST_RIGHT = 2
HOST_LEFT = 3

class Host:
    def __init__(self, sizes, game_display):
        self.sizes = sizes
        self.game_display = game_display
        self.host_position = 0
        self.host_move = HOST_RIGHT
        self.host = pygame.image.load('./media/host.png')
        self.host = pygame.transform.scale(self.host, (math.ceil(self.sizes.display_height/4),math.ceil(self.sizes.display_width/4)))
        self.host_flip = pygame.image.load('./media/host_flip.png')
        self.host_flip = pygame.transform.scale(self.host_flip, (math.ceil(self.sizes.display_height/4),math.ceil(self.sizes.display_width/4)))

    def display_host(self):
        if self.host_move > 1:
            if self.host_move == HOST_RIGHT:
                self.host_right()
            else:
                self.host_left()
        else:
            if self.host_move == HOST_STOP_RIGHT:
                self.game_display.blit(self.host_flip,(590,(self.sizes.game_title_height)))
            else:
                self.game_display.blit(self.host,(0,(self.sizes.game_title_height)))

    def host_right(self):
        if self.host_position < 600:
            self.game_display.blit(self.host,(self.host_position,(self.sizes.game_title_height)))
            self.host_position += 10
        else:
            self.game_display.blit(self.host_flip,(590,(self.sizes.game_title_height))) # Change static '590'
            self.host_move = HOST_STOP_RIGHT

    def host_left(self):
        if self.host_position > 10:
            self.game_display.blit(self.host_flip,(self.host_position,(self.sizes.game_title_height)))
            self.host_position -= 10
        else:
            self.game_display.blit(self.host,(10,(self.sizes.game_title_height)))
            self.host_move = HOST_STOP_LEFT

    def host_move_side(self):
        if self.host_move == HOST_STOP_LEFT or self.host_move == HOST_LEFT:
            self.host_move = HOST_RIGHT
        elif self.host_move == HOST_STOP_RIGHT or self.host_move == HOST_RIGHT:
            self.host_move = HOST_LEFT
        else:
            raise Exception('Error: Host is in an invalid move state.')