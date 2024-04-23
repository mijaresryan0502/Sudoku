import pygame
from constants import *

class Cell:
    #Constructor
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.red = False
        self.sketched_value = 0.1
        self.cell_value = 0.1
    #Setters
    def set_cell_value(self, value):
        self.cell_value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        #Draws lines for the cell
        pygame.draw.rect(self.screen, LINE_COLOR, (self.row * SQUARE_SIZE, self.col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)

        #Draws the number for the random number for the cell
        if self.value > 0 and self.sketched_value == 0.1:
            num_font = pygame.font.Font(None, 75)
            num_surface = num_font.render(str(self.value), 0, TEXT_COLOR)
            #Draws the number at the center of the cell
            num_rect = num_surface.get_rect(
                center = (
                    self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                    self.row * SQUARE_SIZE + SQUARE_SIZE // 2)
            )
            self.screen.blit(num_surface, num_rect)

        #Draws "notes" for user (Smaller numbers not definite answer) on the top left of the box
        elif self.sketched_value > 0.1 and self.cell_value == 0.1:
            pygame.draw.rect(self.screen, BG_COLOR,
                (self.col * SQUARE_SIZE + SQUARE_SIZE * 0.18, self.row * SQUARE_SIZE + SQUARE_SIZE * 0.18, SQUARE_SIZE // 4, SQUARE_SIZE // 4))
            num_font = pygame.font.Font(None, 25)
            num_surface = num_font.render(str(self.sketched_value), 0, SKETCH_COLOR)
            #Draws the number at the top left of the cell
            num_rect = num_surface.get_rect(
                center = (
                    self.col * SQUARE_SIZE + SQUARE_SIZE // 4,
                    self.row * SQUARE_SIZE + SQUARE_SIZE // 4)
            )
            self.screen.blit(num_surface, num_rect)

        #Draws the user input when enter is clicked
        elif self.cell_value > 0.1:
            pygame.draw.rect(self.screen, BG_COLOR,
                (self.col * SQUARE_SIZE + SQUARE_SIZE * 0.1, self.row * SQUARE_SIZE + SQUARE_SIZE * 0.1, SQUARE_SIZE // 1.5, SQUARE_SIZE // 1.5))
            num_font = pygame.font.Font(None, 75)
            num_surface = num_font.render(str(self.cell_value), 0, TEXT_COLOR)
            #Draws the number at the center of the cell
            num_rect = num_surface.get_rect(
                center= (
                    self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                    self.row * SQUARE_SIZE + SQUARE_SIZE // 2)
            )
            self.screen.blit(num_surface, num_rect)

        #If nothing is in the cell it will have no number
        elif self.cell_value == 0 and self.sketched_value == 0:
            pygame.draw.rect(self.screen, BG_COLOR,
                (self.col * SQUARE_SIZE + SQUARE_SIZE * 0.18, self.row * SQUARE_SIZE + SQUARE_SIZE * 0.18, SQUARE_SIZE // 2, SQUARE_SIZE // 2))

        #If user clicked box highlight the box in red
        if self.red == True:
            pygame.draw.rect(self.screen, BOX_COLOR,
                (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)

        #Updates the display
        pygame.display.update()
