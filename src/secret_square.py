import pygame
import math
from employee import Employee
from text import Text
from random import randrange

class SecretSquare:
    def __init__(self, sizes, game_display):
        self.sizes = sizes
        self.game_display = game_display

        self.random_square = randrange(9)
        print(self.random_square)
        self.found = False

        self.width = math.ceil(sizes.display_width/5)
        self.length = math.ceil(sizes.display_height/5)
        self.center_width = math.ceil((((self.sizes.display_width-self.sizes.grid_size)*(self.sizes.grid_fraction)) - self.width) / 2)
        self.center_length = math.ceil((self.sizes.display_height - self.length) / 2)

        self.gift_card = pygame.image.load('./media/amazon_gift_card.png')
        self.gift_card = pygame.transform.scale(self.gift_card, (self.width, self.length))

        self.message_1 = Text('', 2*sizes.text_size, game_display, self.center_width + math.ceil(self.width/2), self.center_length + self.length + (2*sizes.text_size))
        self.message_2 = Text('and a $10 Amazon giftcard!', 2*sizes.text_size, game_display, self.center_width + math.ceil(self.width/2), self.center_length + self.length + (5*sizes.text_size))
    
    def is_secret_square(self, employee, winner):
        if self.found:
            return
        if not isinstance(employee, Employee):
            raise Exception('Error: Should use employee object.')
        if employee.order == self.random_square:
            self.found = True
            self.message_1.change_text(winner + ', you won the secret square')
            pygame.mixer.music.load("./media/sfx/yay.mp3")
            pygame.mixer.music.play(loops=0)
            return True
        return False

    def display_gift_card(self):
        self.game_display.blit(self.gift_card,(self.center_width, self.center_length))
        self.message_1.message_display()
        self.message_2.message_display()
