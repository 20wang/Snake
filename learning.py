# much assistance from here: https://www.101computing.net/getting-started-with-pygame/

import pygame
import random
from Snake import Snake
from Thinker import Thinker
pygame.init()

# define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# create game window
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brain Snake")

thinker = Thinker()

newGame = True
while newGame:
    all_sprites_list = pygame.sprite.Group()

    player = Snake(GREEN)

    playing = True
    clock = pygame.time.Clock()

    direction = 'U'

    score = 0

    working = True
    while working:
        x = random.randint(0, 24) * 20
        y = random.randint(0, 24) * 20
        working = player.checkWin(x, y)

    newX = x
    newY = y
    add = False

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                newGame = False

        direction = thinker.getDirection()

        player.update(direction)

        if add:
            player.add(newX, newY)
            add = False

        screen.fill(BLACK)

        pygame.draw.rect(screen, YELLOW, [x, y, 20, 20])

        for body in player.snake:
            pygame.draw.rect(screen, player.color, [body.x, body.y, body.width, body.height])
        pygame.display.flip()

        if player.checkLose():
            playing = False

        if player.checkWin(x, y):
            newX = x
            newY = y
            add = True

            working = True
            while working:
                x = random.randint(0, 24) * 20
                y = random.randint(0, 24) * 20
                working = player.checkWin(x, y)
            score += 1

        clock.tick(10)

    print()
    print('-------- GAME OVER --------')
    print('your score: ' + str(score))
