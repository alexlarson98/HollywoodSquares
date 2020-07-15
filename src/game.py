import pygame
import math
from text import Text
from host import Host
from end_screen import EndScreen
from player import Player
from grid import Grid
from button import Button
from employee import Emmployee

START = 1
CHOOSE_CELEBRITY = 2
ASK_QUESTION = 3
MARK_GRID = 4
CHECK_WINNER = 5
END = 6

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

        # Grid
        self.grid = Grid(sizes)

        # Game state
        self.game_state = START

        # Winner
        self.winner = None

        # Initialize players in game
        self.player_x = Player('./media/kayla_rice.jpg', "Player X", sizes)
        self.player_o = Player('./media/steve_carey.jpg', "Player O", sizes)

        # Discribes whether player x or player o is active
        self.current_player = self.player_x

        # Currently selected employee
        self.current_employee = None

        # End screen
        self.end_screen = EndScreen(game_display, sizes)

        # Set location of employees to rectangles based on display
        self.set_rectangles()

        # Set messages
        self.annoouncer_message = Text('', game_display, (((self.sizes.display_width-self.sizes.grid_size) * self.sizes.grid_fraction))/2, self.sizes.game_title_height+24)
        self.annoouncer_warning = Text('', game_display, (((self.sizes.display_width-self.sizes.grid_size) * self.sizes.grid_fraction))/2, self.sizes.game_title_height, color=(255,0,0))

        # Colors
        self.black = (0,0,0)
        self.green = (0,128,0)
        self.dark_green = (0,75,0)
        self.red = (255,0,0)
        self.dark_red = (128,0,0)

        # Set hosts
        self.host = Host(sizes, game_display)

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
        self.annoouncer_warning.message_display()

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
                self.game_state = CHOOSE_CELEBRITY
                self.active_game = True
                self.host.host_move_side()

    # Check if position clicked is in an employee square
    def in_square(self, pos):
        if self.game_state != CHOOSE_CELEBRITY:
            return
        for employee in self.employees:
            if employee.rectangle.collidepoint(pos[0],pos[1]):
                if self.check_valid(employee.name):
                    self.current_employee = employee
                    self.game_state = ASK_QUESTION
                    employee.set_not_available()
                    self.annoouncer_warning.change_text('')
                else:
                    self.annoouncer_warning.change_text(employee.name + ' is not available!')

    def in_button(self, pos):
        if self.game_state != ASK_QUESTION:
            return
        if self.correct_button.isOver(pos):
            self.current_employee.x_or_o = self.current_player.get_letter()
            self.game_state = MARK_GRID

        elif self.incorrect_button.isOver(pos):
            self.current_employee.x_or_o = self.current_player.get_opposite_letter()  
            self.game_state = MARK_GRID     

    # Swap current player
    def swap_current_player(self):
        if self.current_player == self.player_x:
            self.current_player = self.player_o
        else:
            self.current_player = self.player_x

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

    def choose_celebrity(self):
        if not self.is_active():
            raise Exception('Error: Game is not active, so the game cannot be executed')

        self.annoouncer_message.change_text(self.current_player.name + ', please choose an available celebrity!')

    def ask_question(self):
        if not self.is_active():
            raise Exception('Error: Game is not active, so the game cannot be executed')
        self.annoouncer_message.change_text('Question for ' + self.current_employee.name +':')
        self.grid.set_player_index(self.current_employee.order)

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

    def display_board(self):
        self.grid.display_grid(self.game_display)

    def get_board(self):
        return [employee.x_or_o for employee in self.employees]

    def check_horizontal(self, l):
        for i in range(0,8,3):
            horizontal = l[i:i+3]
            if len(set(horizontal)) == 1 and None not in horizontal:
                if "X" in horizontal:
                    self.winner = self.player_x
                else:
                    self.winner = self.player_o

    def check_vertical(self, l):
        for i in range(3):
            vertical = l[i::3]
            if len(set(vertical)) == 1 and None not in vertical:
                if "X" in vertical:
                    self.winner = self.player_x
                else:
                    self.winner = self.player_o

    def check_diagonal(self, l):
        diagonal = l[0::4]
        if len(set(diagonal)) == 1 and None not in diagonal:
            if "X" in diagonal:
                self.winner = self.player_x
            else:
                self.winner = self.player_o
        diagonal = l[2::2][0:3]
        if len(set(diagonal)) == 1 and None not in diagonal:
            if "X" in diagonal:
                self.winner = self.player_x
            else:
                self.winner = self.player_o

    def check_five(self, board):
        if board.count('X') >= 5:
            self.winner = self.player_x
        if board.count('O') >= 5:
            self.winner = self.player_o

    def check_winner(self):
        board = self.get_board()
        self.check_five(board)
        self.check_vertical(board)
        self.check_horizontal(board)
        self.check_diagonal(board)
        self.grid.reset_player_index()

        if self.winner:
            self.game_state = END
            self.active_game = False
            self.annoouncer_message.change_text(self.winner.name + ' wins!')
            self.end_screen.set_winner(self.winner)
        else:
            self.swap_current_player()
            self.host.host_move_side()
            self.game_state = CHOOSE_CELEBRITY

    def display_host(self):
        self.host.display_host()

    def draw_x_and_o(self):
        for employee in self.employees:
            if employee.get_x_or_o():
                employee.draw(self.game_display)

    def end(self):
        self.current_employee = None
        self.winner = None
        self.end_screen.end_game()
        