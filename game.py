import pygame
import math
from text import Text
from button import Button
from employee import Emmployee

START = 1
CHOOSE_CONTESTANT = 2
ASK_QUESTION = 3
MARK_GRID = 4
CHECK_WINNER = 5
END = 6

HOST_STOP_LEFT = 0
HOST_STOP_RIGHT = 1
HOST_RIGHT = 2
HOST_LEFT = 3


class Game():
    def __init__(self, game_display, sizes):  
        # Game metrics
        self.sizes = sizes
        self.game_display = game_display

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
        self.game_state = START

        # Winner
        self.winner = None

        # Discribes whether player x or player o is active
        self.current_player = "Player X"

        # Currently selected employee
        self.current_employee = None

        # Set location of employees to rectangles based on display
        self.set_rectangles()

        # Set messages
        self.annoouncer_message = Text('', game_display, (((self.sizes.display_width-self.sizes.grid_size) * self.sizes.grid_fraction))/2, self.sizes.game_title_height)

        # Colors
        self.black = (0,0,0)
        self.green = (0,128,0)
        self.dark_green = (0,75,0)
        self.red = (255,0,0)
        self.dark_red = (128,0,0)

        # Set hosts
        self.host_position = 0
        self.host_move = HOST_RIGHT
        self.host = pygame.image.load('./media/host.png')
        self.host = pygame.transform.scale(self.host, (math.ceil(self.sizes.display_height/4),math.ceil(self.sizes.display_width/4)))
        self.host_flip = pygame.image.load('./media/host_flip.png')
        self.host_flip = pygame.transform.scale(self.host_flip, (math.ceil(self.sizes.display_height/4),math.ceil(self.sizes.display_width/4)))

        # Set start button
        self.start_button = pygame.image.load('./media/start_button.png')
        self.start_button = pygame.transform.scale(self.start_button, (self.sizes.start_button_width, self.sizes.start_button_height))
        self.start_button_rect = pygame.Rect(self.center_from_grid_x(self.sizes.start_button_width), self.sizes.game_title_height + self.sizes.start_button_height, self.sizes.start_button_width, self.sizes.start_button_height)

        # Set start button
        self.start_button = pygame.image.load('./media/start_button.png')
        self.start_button = pygame.transform.scale(self.start_button, (self.sizes.start_button_width, self.sizes.start_button_height))
        self.start_button_rect = pygame.Rect(self.center_from_grid_x(self.sizes.start_button_width), self.sizes.game_title_height + self.sizes.start_button_height, self.sizes.start_button_width, self.sizes.start_button_height)

        # Button initializations
        self.correct_button = Button(self.green, 50, sizes.display_height-150, 250, 100, 'CORRECT')
        self.incorrect_button = Button(self.red, sizes.display_width-300, sizes.display_height-150, 250, 100, 'INCORRECT')

    def display_start_button(self):
        if self.game_state != START:
            raise Exception('Error: Can\t display start button if not in start mode.')
        self.game_display.blit(self.start_button, ( self.center_from_grid_x(self.sizes.start_button_width) , self.sizes.game_title_height + self.sizes.start_button_height))

    # Display all messages for game
    def display_all_messages(self):
        # self.annoouncer_message.drawText()
        self.annoouncer_message.message_display()

    # Assign rectangle space for each employee in the game
    def set_rectangles(self):
        for employee in self.employees:
            if employee.order < 3:
                employee.set_rectangle(
                                      ((self.sizes.display_width-self.sizes.grid_size) * self.sizes.grid_fraction) + (employee.order * self.sizes.grid_increment),
                                      ((self.sizes.display_height-self.sizes.grid_size) / 2),
                                      self.sizes.grid_increment
                                      )
            elif employee.order < 6:
                employee.set_rectangle(
                                      ((self.sizes.display_width-self.sizes.grid_size) * self.sizes.grid_fraction) + ((employee.order-3) * self.sizes.grid_increment),
                                      ((self.sizes.display_height-self.sizes.grid_size) / 2) + self.sizes.grid_increment,
                                      self.sizes.grid_increment
                                      )
            elif employee.order < 9:
                employee.set_rectangle(
                                      ((self.sizes.display_width-self.sizes.grid_size) * self.sizes.grid_fraction) + ((employee.order-6) * self.sizes.grid_increment),
                                      ((self.sizes.display_height-self.sizes.grid_size) / 2) + (2 * self.sizes.grid_increment),
                                      self.sizes.grid_increment
                                      )
            else:
                raise Exception('Error: Squares out of bounds')

    # Draw Hollywood Squares
    def draw_squares(self, display):
        for employee in self.employees:
            pygame.draw.rect(display, (255,255,255), employee.rectangle)

    def button_hover_check(self, pos):
        if self.correct_button.isOver(pos):
            self.correct_button.color = self.dark_green
        else:
            self.correct_button.color = self.green
        if self.incorrect_button.isOver(pos):
            self.incorrect_button.color = self.dark_red
        else:
            self.incorrect_button.color = self.red

    def display_buttons(self):
        self.correct_button.draw(self.game_display)
        self.incorrect_button.draw(self.game_display)

    def start(self, pos):
        if self.game_state == START:
            if self.start_button_rect.collidepoint(pos[0],pos[1]):
                self.game_state = CHOOSE_CONTESTANT
                self.active_game = True
                self.host_move_side()

    # Check if position clicked is in an employee square
    def in_square(self, pos):
        if self.game_state != CHOOSE_CONTESTANT:
            return
        for employee in self.employees:
            if employee.rectangle.collidepoint(pos[0],pos[1]):
                if self.check_valid(employee.name):
                    self.current_employee = employee
                    self.game_state = ASK_QUESTION
                    return
                else:
                    self.annoouncer_message.change_text('Please choose a different contestant! ' + employee.name + ' is not available.')

    def in_button(self, pos):
        if self.game_state != ASK_QUESTION:
            return
        if self.correct_button.isOver(pos):
            if self.current_player == "Player X":
                self.current_employee.x_or_o = "X"
            elif self.current_player == "Player O":
                self.current_employee.x_or_o = "O"
            else:
                raise Exception("Error: Invalid player type.")
            self.game_state = MARK_GRID

        elif self.incorrect_button.isOver(pos):
            if self.current_player == "Player X":
                self.current_employee.x_or_o = "O"
            elif self.current_player == "Player O":
                self.current_employee.x_or_o = "X"
            else:
                raise Exception("Error: Invalid player type.")    
            self.game_state = MARK_GRID     

    # Swap current player
    def swap_current_player(self):
        if self.current_player == "Player X":
            self.current_player = "Player O"
        else:
            self.current_player = "Player X"

    def center_from_grid_x(self, object_length):
        return ( ( (self.sizes.display_width-self.sizes.grid_size)*(self.sizes.grid_fraction) ) - object_length) / 2

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
        if not self.is_active():
            raise Exception('Error: Game is not active, so the game cannot be executed')
        self.annoouncer_message.change_text(self.current_player + ', please choose an available contestant!')

    def ask_question(self):
        if not self.is_active():
            raise Exception('Error: Game is not active, so the game cannot be executed')
        self.annoouncer_message.change_text('Question for ' + self.current_employee.name +':')

    # Called after 'CORRECT' or 'INCORRECT' button is clicked by user
    def mark_grid(self):
        if self.current_employee.x_or_o == "X":
            self.current_employee.set_shape('./media/x.png')
            self.game_state = CHECK_WINNER
        elif self.current_employee.x_or_o == "O":
            self.current_employee.set_shape('./media/o.png')
            self.game_state = CHECK_WINNER
        else:
            raise Exception('Error: cannot mark grid if a shape for the employee does not exist.')

    def get_board(self):
        return [employee.x_or_o for employee in self.employees]

    def check_horizontal(self, l):
        for i in range(0,8,3):
            horizontal = l[i:i+3]
            if len(set(horizontal)) == 1 and None not in horizontal:
                if "X" in horizontal:
                    self.winner = "Player X"
                else:
                    self.winner = "Player O"

    def check_vertical(self, l):
        for i in range(3):
            vertical = l[i::3]
            if len(set(vertical)) == 1 and None not in vertical:
                if "X" in vertical:
                    self.winner = "Player X"
                else:
                    self.winner = "Player O"

    def check_diagonal(self, l):
        diagonal = l[0::4]
        if len(set(diagonal)) == 1 and None not in diagonal:
            if "X" in diagonal:
                self.winner = "Player X"
            else:
                self.winner = "Player O"
        diagonal = l[2::2][0:3]
        if len(set(diagonal)) == 1 and None not in diagonal:
            if "X" in diagonal:
                self.winner = "Player X"
            else:
                self.winner = "Player O"

    def check_five(self, board):
        if board.count('X') >= 5:
            self.winner = "Player X"
        if board.count('O') >= 5:
            self.winner = "Player O"

    def check_winner(self):
        board = self.get_board()
        self.check_five(board)
        self.check_vertical(board)
        self.check_horizontal(board)
        self.check_diagonal(board)

        if self.winner:
            self.game_state = END
            self.active_game = False
        else:
            self.swap_current_player()
            self.host_move_side()
            self.game_state = CHOOSE_CONTESTANT

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
        if self.host_position > 0:
            self.game_display.blit(self.host_flip,(self.host_position,(self.sizes.game_title_height)))
            self.host_position -= 10
        else:
            self.game_display.blit(self.host,(0,(self.sizes.game_title_height)))
            self.host_move = HOST_STOP_LEFT

    def host_move_side(self):
        if self.host_move == HOST_STOP_LEFT or self.host_move == HOST_LEFT:
            self.host_move = HOST_RIGHT
        elif self.host_move == HOST_STOP_RIGHT or self.host_move == HOST_RIGHT:
            self.host_move = HOST_LEFT
        else:
            raise Exception('Error: Host is in an invalid move state.')

    def draw_x_and_o(self):
        for employee in self.employees:
            if employee.get_x_or_o():
                employee.draw(self.game_display)

    def end(self):
        self.current_employee = None
        self.winner = None
        
