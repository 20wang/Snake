# a version of Q-learning snake slow enough for the user to watch
# 3-3-2020
__author__ = '20wang'

import pygame
import random
from snake import Snake
from thinker import Thinker
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

thinker = Thinker(0, 0)

metadata = []

newGame = True
coins = 0
while newGame and coins < 10:
    all_sprites_list = pygame.sprite.Group()

    player = Snake(GREEN)

    playing = True
    clock = pygame.time.Clock()

    direction = 'U'

    score = 0

    # create food
    working = True
    while working:
        x = random.randint(0, 24) * 20
        y = random.randint(0, 24) * 20
        working = player.checkWin(x, y)

    newX = x
    newY = y
    add = False

    # terminate program if window closed
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                newGame = False

        # get input from Q-learning algorithm
        direct = thinker.getDirect(x, y, player.snake, direction)
        if direct == 'L' and direction != 'R':
            direction = 'L'
        elif direct == 'R' and direction != 'L':
            direction = 'R'
        elif direct == 'U' and direction != 'D':
            direction = 'U'
        elif direct == 'D' and direction != 'U':
            direction = 'D'

        player.update(direction)

        if add:
            player.add(newX, newY)
            add = False

        # draw everything
        screen.fill(BLACK)

        pygame.draw.rect(screen, YELLOW, [x, y, 20, 20])

        for body in player.snake:
            pygame.draw.rect(screen, player.color, [body.x, body.y, body.width, body.height])
        pygame.display.flip()

        if player.checkLose():
            playing = False
            thinker.learn(-10)

        if player.checkWin(x, y):
            newX = x
            newY = y
            add = True

            # create new food
            working = True
            while working:
                x = random.randint(0, 24) * 20
                y = random.randint(0, 24) * 20
                working = player.checkWin(x, y)
            score += 1
            thinker.learn(10)

        clock.tick(20)

    thinker.record()
    coins += 1

    print()
    print('game ' + str(coins) + ' score: ' + str(score))