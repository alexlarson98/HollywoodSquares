import pygame
import math
from text import Text
from employee import Emmployee

HOME = 0
START = 1
CHOOSE_CONTESTANT = 2
ASK_QUESTION = 3
MARK_GRID = 4
CHECK_WINNER = 5
END = 6


class Game():
    def __init__(self, game_display, sizes):  
        # Game metrics
        self.game_display = game_display
        self.display_height = sizes.display_height
        self.display_width = sizes.display_width
        self.grid_size = sizes.grid_size
        self.grid_fraction = sizes.grid_fraction
        self.grid_increment = math.ceil(sizes.grid_size/3)
        self.game_title_width = sizes.game_title_width
        self.game_title_height = sizes.game_title_height

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

        # Game state
        self.game_state = HOME

        # Discribes whether player x or player o is active
        self.current_player = "Player X"

        # Currently selected employee
        self.current_employee = None

        # Set location of employees to rectangles based on display
        self.set_rectangles()

        # Set messages
        test = Text('Press any key to continue!', game_display, (((self.display_width-self.grid_size) * self.grid_fraction))/2, self.display_height-30)
        self.annoouncer_message = Text('teststtstststsssssssssssssssssssssssssssssss', game_display, (((self.display_width-self.grid_size) * self.grid_fraction))/2, self.game_title_height)

    # Display all messages for game
    def display_all_messages(self):
        # self.annoouncer_message.drawText()
        self.annoouncer_message.message_display()

    # Assign rectangle space for each employee in the game
    def set_rectangles(self):
        for employee in self.employees:
            if employee.order < 3:
                employee.set_rectangle(
                                      ((self.display_width-self.grid_size) * self.grid_fraction) + (employee.order * self.grid_increment),
                                      ((self.display_height-self.grid_size) / 2),
                                      self.grid_increment
                                      )
            elif employee.order < 6:
                employee.set_rectangle(
                                      ((self.display_width-self.grid_size) * self.grid_fraction) + ((employee.order-3) * self.grid_increment),
                                      ((self.display_height-self.grid_size) / 2) + self.grid_increment,
                                      self.grid_increment
                                      )
            elif employee.order < 9:
                employee.set_rectangle(
                                      ((self.display_width-self.grid_size) * self.grid_fraction) + ((employee.order-6) * self.grid_increment),
                                      ((self.display_height-self.grid_size) / 2) + (2 * self.grid_increment),
                                      self.grid_increment
                                      )
            else:
                raise Exception('Error: Squares out of bounds')

    # Draw Hollywood Squares
    def draw_squares(self, display):
        for employee in self.employees:
            pygame.draw.rect(display, (255,255,255), employee.rectangle)

    # Check if position clicked is in an employee square
    def in_square(self, pos):
        # if self.game_state != "CHOOSE_CONTESTANT":
        #     return
        for employee in self.employees:
            if employee.rectangle.collidepoint(pos[0],pos[1]):
                print(employee.name)
                if not self.check_valid(employee.name):
                    self.game_state = ASK_QUESTION
                    return
                else:
                    self.annoouncer_message.change_text('Please choose a different contestant! ' + employee.name + ' is not available.')
                    print('Please choose a different contestant!\n', employee.name, 'is not available.')

    # Swap current player
    def swap_current_player(self):
        if self.current_player == "Player X":
            self.current_player = "Player O"
        else:
            self.current_player = "Player X"

    # Check if player clicked is available
    def check_valid(self, name):
        for employee in self.employees:
            if employee.name == name:
                if not employee.is_available():
                    return False
                else:
                    return True

    # Check if there's an active game
    def is_active(self):
        return self.active_game

    def choose_contestant(self):
        # if not self.is_active():
        #     raise Exception('Error: Game is not active, so the game cannot be executed')
        # if self.game_state ==
        top_text = self.current_player + ', please choose an available contestant!'
        self.game_state = CHOOSE_CONTESTANT
        print(top_text)

    def ask_question(self):
        # top_text = self.current_player + ', please choose an available contestant!'
        self.game_state = ASK_QUESTION

    def mark_grid(self):
        self.game_state = MARK_GRID

    def check_winner(self):
        self.game_state = CHECK_WINNER

