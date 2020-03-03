# makes moves and learns new states using Q-learning
# 3-3-2020
__author__ = '20wang'

# much assistance from here: https://towardsdatascience.com/q-learning-54b841f3f9e4

from random import randint


class Thinker(object):

    # class constructor
    def __init__(self, rando, rate):
        self.moves = []
        self.states = [line.rstrip('\n') for line in open('states')]
        for i in range(0, len(self.states)):
            self.states[i] = self.states[i].split(',')
        self.rando = rando
        self.rate = rate
        self.moveset = ['U', 'D', 'L', 'R']

    # gets a direction based on current state
    def getDirect(self, goalX, goalY, snake, direction):
        direct = 'U'
        posX = snake[len(snake) - 1].x
        posY = snake[len(snake) - 1].y

        goalU = False
        goalD = False
        goalL = False
        goalR = False

        if goalX > posX:
            goalR = True
        if goalX < posX:
            goalL = True
        if goalY > posY:
            goalD = True
        if goalY < posY:
            goalU = True

        obsR = False
        obsL = False
        obsD = False
        obsU = False

        for i in range(len(snake) - 2):
            b = snake[i]
            if b.x == 20 + posX and b.y == posY:
                obsR = True
            elif b.x == posX - 20 and b.y == posY:
                obsL = True
            elif b.x == posX and b.y == posY + 20:
                obsD = True
            elif b.x == posX and b.y == posY - 20:
                obsU = True

        if posY == 0:
            obsU = True
        if posY == 480:
            obsD = True
        if posX == 0:
            obsL = True
        if posX == 480:
            obsR = True

        data = [direction, goalU, goalD, goalL, goalR, obsR, obsL, obsD, obsU]
        encoded = self.encode(data)


        state = []
        for line in range(len(self.states)):
            if self.states[line][0] == encoded:
                state = self.states[line]
                break

        r = randint(0, 1000)
        if self.rando > r or state == []:
            m = randint(1, 4)
            self.moves.append([encoded, m])
            return self.moveset[m - 1]
        if self.rando > 50:
            self.rando -= 1

        maximum = 1
        for v in range(1, 5):
            if float(state[v]) > float(state[maximum]):
                maximum = v

        direct = self.moveset[maximum - 1]

        self.moves.append([encoded, maximum])
        return direct

    # converts direction, food position, obstacles to a string
    def encode(self, data):
        encoded = ""
        encoded += data[0]
        for x in range(1, len(data)):
            if data[x]:
                encoded += 'T'
            elif not data[x]:
                encoded += 'F'
        return encoded

    # applies success/failure score to entry in states
    def learn(self, score):
        for state in self.states:
            for move in self.moves:
                if move[0] == state[0]:
                    state[move[1]] = float(state[move[1]]) * (1 - self.rate) + score * self.rate
                    self.moves.remove(move)

        for m in self.moves:
            self.states.append([m[0], 0.0, 0.0, 0.0, 0.0])
            self.states[len(self.states) - 1][m[1]] = score * self.rate
            self.moves.remove(m)

    # records states in a text file
    def record(self):
        f = open('states', 'w')
        for line in self.states:
            l = []
            for x in line:
                l.append(str(x))
            f.write(','.join(l) + '\n')
        f.close()
