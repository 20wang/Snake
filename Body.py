import pygame
WHITE = (255, 255, 255)


class Body(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
