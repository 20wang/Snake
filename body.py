# object that represents a pixel of the snake's body
# 3-3-2020
__author__ = '20wang'

import pygame
WHITE = (255, 255, 255)


class Body(pygame.sprite.Sprite):

    # class constructor
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
