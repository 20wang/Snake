from Body import Body
import pygame
WHITE = (255, 255, 255)


class Snake(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.snake = [Body(color, 20, 20, 240, 320), Body(color, 20, 20, 240, 300), Body(color, 20, 20, 240, 280), Body(color, 20, 20, 240, 260), Body(color, 20, 20, 240, 240)]
        self.color = color

    def update(self, direction):
        if direction == 'U':
            self.snake.append(Body(self.color, 20, 20,
                                   self.snake[len(self.snake) - 1].x, self.snake[len(self.snake) - 1].y - 20))
            del self.snake[0]
        elif direction == 'D':
            self.snake.append(Body(self.color, 20, 20,
                                   self.snake[len(self.snake) - 1].x, self.snake[len(self.snake) - 1].y + 20))
            del self.snake[0]
        elif direction == 'R':
            self.snake.append(Body(self.color, 20, 20,
                                   self.snake[len(self.snake) - 1].x + 20, self.snake[len(self.snake) - 1].y))
            del self.snake[0]
        elif direction == 'L':
            self.snake.append(Body(self.color, 20, 20,
                                   self.snake[len(self.snake) - 1].x - 20, self.snake[len(self.snake) - 1].y))
            del self.snake[0]

    def checkLose(self):
        x = self.snake[len(self.snake) - 1].x
        y = self.snake[len(self.snake) - 1].y
        if x >= 500 or x < 0:
            return True
        if y >= 500 or y < 0:
            return True

        for b in range(len(self.snake) - 1):
            if self.snake[b].x == x and self.snake[b].y == y:
                return True

        return False

    def checkWin(self, x, y):
        for b in range(len(self.snake)):
            if self.snake[b].x == x and self.snake[b].y == y:
                return True

    def add(self, x, y):
        self.snake.insert(0, Body(self.color, 20, 20, x, y))