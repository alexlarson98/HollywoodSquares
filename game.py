import pygame
import math

PLAYER_O = 0
PLAYER_X = 1

class Emmployee():
    def __init__(self, name, order, x_or_o=None):
        self.name = name
        self.order = order
        self.x_or_o = x_or_o
        self.is_available = True
        self.rectangle = None

    def is_available(self):
        return self.is_available

    def set_rectangle(self, x, y, box_size):
        self.rectangle = pygame.Rect(x, y, box_size, box_size)


class Game():
    def __init__(self, display_width, display_height, grid_size):  
        # Game metrics
        self.display_height = display_height
        self.display_width = display_width
        self.grid_size = grid_size
        self.grid_increment = math.ceil(grid_size/3)

        # Initialize employees aactive in the game
        self.employees = [
            Emmployee('Ann', 0),
            Emmployee('Wanda', 1),
            Emmployee('Susan', 2),
            Emmployee('Nick', 3),
            Emmployee('Donna', 4),
            Emmployee('Tiffany', 5),
            Emmployee('Sara R.', 6),
            Emmployee('Brendan', 7),
            Emmployee('Sarah L.', 8),
        ]

        # Is a game currently active
        self.active_game = False

        # Discribes whether player x or player o is active
        self.current_player = 0

        self.set_rectangles()

    # Assign rectangle space for each employee in the game
    def set_rectangles(self):
        for employee in self.employees:
            if employee.order < 3:
                employee.set_rectangle(
                                      ((self.display_width-self.grid_size) / 2) + (employee.order * self.grid_increment),
                                      ((self.display_height-self.grid_size) / 2),
                                      self.grid_increment
                                      )
                print('first',employee.name, ((self.display_width-self.grid_size) / 2) + (employee.order * self.grid_increment), ((self.display_height-self.grid_size) / 2), self.grid_increment)
            elif employee.order < 6:
                employee.set_rectangle(
                                      ((self.display_width-self.grid_size) / 2) + ((employee.order-3) * self.grid_increment),
                                      ((self.display_height-self.grid_size) / 2) + self.grid_increment,
                                      self.grid_increment
                                      )
                print('sec',employee.name, ((self.display_width-self.grid_size) / 2) + ((employee.order-3) * self.grid_increment), ((self.display_height-self.grid_size) / 2), self.grid_increment)
            elif employee.order < 9:
                employee.set_rectangle(
                                      ((self.display_width-self.grid_size) / 2) + ((employee.order-6) * self.grid_increment),
                                      ((self.display_height-self.grid_size) / 2) + (2 * self.grid_increment),
                                      self.grid_increment
                                      )
                print('third',employee.name, ((self.display_width-self.grid_size) / 2) + ((employee.order-6) * self.grid_increment), ((self.display_height-self.grid_size) / 2), self.grid_increment)
            else:
                raise Exception('Error: Squares out of bounds')

    # Draw Hollywood Squares
    def draw_squares(self, display):
        for employee in self.employees:
            pygame.draw.rect(display, (255,255,255), employee.rectangle)

    def in_square(self, pos):
        for employee in self.employees:
            if employee.rectangle.collidepoint(pos[0],pos[1]):
                print(employee.name)

    # Swap current player
    def swap_current_player(self):
        if not self.current_player:
            self.current_player = 1
        else:
            self.current_player = 0

    def check_valid(self, pos):
    #     for employee in self.employees:
    #         if employee.is_available():
        pass

    # Check if there's an active game
    def is_active(self):
        return self.active_game
                

