import pygame
from constants import *
#imports needed packages
pygame.init()

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch = 11
        self.selected = False
        self.width = 60
        self.height = 60
        #if the value when initailized is not 0 it locks the cell so that it cant be edited
        if value != 0:
            self.locked = True
        else:
            self.locked = False

    def set_cell_value(self, value):
        self.value = value
        self.sketch = 0
        #takes the sketch value and sets the value equal to it then sets sketch to 0

    def get_sketch(self):
        return self.sketch
        #returns sketch value

    def set_sketched_value(self, value):
        self.sketch = value
        #sets sketch value to value
    def get_value(self):
        return self.value
    #returns value
    def get_locked(self):
        return self.locked
    #returns locked value
    def draw(self):

        num_font = pygame.font.Font(None, 30)
        for num in range(10):
            num_surf = num_font.render(str(num), True, BLACK)
            if self.sketch == num and num != 0:
                pygame.draw.rect(self.screen, (255, 255, 255),pygame.Rect(self.row * SQUARE_SIZE + 5, self.col * SQUARE_SIZE + 5, SQUARE_SIZE - 10,SQUARE_SIZE - 10), 30)
                num_rect = num_surf.get_rect(
                    center=(SQUARE_SIZE * self.row + SQUARE_SIZE // 3, SQUARE_SIZE * self.col + SQUARE_SIZE // 3))
                self.screen.blit(num_surf, num_rect)
        #for loop so if num is equal to the sketch value it prints it out onto the screen... probably

        #draw value
        num_font = pygame.font.Font(None, 50)
        for num in range(10):
            if self.value == num and self.locked:
                num_surf = num_font.render(str(num), True, BLACK)
                num_rect = num_surf.get_rect(
                    center=(SQUARE_SIZE * self.row + SQUARE_SIZE // 2, SQUARE_SIZE * self.col + SQUARE_SIZE // 2))
                self.screen.blit(num_surf, num_rect)
            elif self.value == num and num != 0:
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 pygame.Rect(self.row * SQUARE_SIZE+5, self.col * SQUARE_SIZE+5, SQUARE_SIZE-10, SQUARE_SIZE-10),
                                 30)
                num_surf = num_font.render(str(num), True, (RED))
                #makes the saved number red for some reason
                num_rect = num_surf.get_rect(
                    center=(SQUARE_SIZE * self.row + SQUARE_SIZE // 2, SQUARE_SIZE * self.col + SQUARE_SIZE // 2))
                self.screen.blit(num_surf, num_rect)
                #prints blank box
            elif self.value == 0 and self.sketch == 0:
                pygame.draw.rect(self.screen, BG_COLOR,
                                 [self.row * SQUARE_SIZE + 10, self.col * SQUARE_SIZE + 10, 45, 45])


        
        
        
