import pygame
import math

HOST_STOP_LEFT = 0
HOST_STOP_RIGHT = 1
HOST_RIGHT = 2
HOST_LEFT = 3
HOST_SPEED = 15

class Host:
    def __init__(self, sizes, game_display, maximum):
        self.sizes = sizes
        self.game_display = game_display

        self.width = math.ceil(self.sizes.display_height/4)
        self.height = math.ceil(self.sizes.display_width/4)

        self.host_position = 0
        self.host_position_min = sizes.buffer_width
        self.host_position_max = maximum - self.width - sizes.buffer_width

        # Start position
        self.host_move = HOST_STOP_LEFT

        self.host = pygame.image.load('./media/cathy.png')
        self.host = pygame.transform.scale(self.host, (self.width, self.height))
        self.host_flip = pygame.image.load('./media/cathy_flip.png')
        self.host_flip = pygame.transform.scale(self.host_flip, (self.width, self.height))

    def display_host(self):
        if self.host_move > 1:
            if self.host_move == HOST_RIGHT:
                self.host_right()
            else:
                self.host_left()
        else:
            if self.host_move == HOST_STOP_RIGHT:
                self.game_display.blit(self.host_flip,(self.host_position_max,(self.sizes.game_title_height)))
            else:
                self.game_display.blit(self.host,(self.host_position_min,(self.sizes.game_title_height)))

    def host_right(self):
        if self.host_position < self.host_position_max:
            self.game_display.blit(self.host,(self.host_position, (self.sizes.game_title_height)))
            self.host_position += HOST_SPEED
        else:
            self.game_display.blit(self.host_flip,(self.host_position_max,(self.sizes.game_title_height)))
            self.host_move = HOST_STOP_RIGHT

    def host_left(self):
        if self.host_position > self.host_position_min:
            self.game_display.blit(self.host_flip,(self.host_position,(self.sizes.game_title_height)))
            self.host_position -= HOST_SPEED
        else:
            self.game_display.blit(self.host,(self.host_position_min,(self.sizes.game_title_height)))
            self.host_move = HOST_STOP_LEFT

    def host_move_side(self):
        if self.host_move == HOST_STOP_LEFT or self.host_move == HOST_LEFT:
            self.host_move = HOST_RIGHT
        elif self.host_move == HOST_STOP_RIGHT or self.host_move == HOST_RIGHT:
            self.host_move = HOST_LEFT
        else:
            raise Exception('Error: Host is in an invalid move state.')