#
# 5-10-2018
__author__ = 'Shan Wang'

import matplotlib.pyplot as plt
import numpy as np

file = [line.rstrip('\n') for line in open('metadata')]
for i in range(0, len(file)):
    file[i] = file[i].split(',')

file2 = [line.rstrip('\n') for line in open('metadata2000')]
for i in range(0, len(file2)):
    file2[i] = file2[i].split(',')

pltX = []
pltY = []

for line in file:
    pltX.append(float(line[0]))
    pltY.append(float(line[1]))

for line in file2:
    pltX.append(float(line[0]) + 1000)
    pltY.append(float(line[1]))

fig = plt.figure()

plt.xticks(np.arange(int(min(pltX)), int(max(pltX)) + 1, 100))
plt.title('Results for 2000 Games')
plt.xlabel('Game')
plt.ylabel('Score')

plt.scatter(pltX, pltY)
plt.show()