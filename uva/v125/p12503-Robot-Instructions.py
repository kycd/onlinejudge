#!/bin/python3
# 1 star
# simulation
# 20571145    12503    Robot Instructions    Accepted    PYTH3    0.040    2018-01-05 09:36:12

import sys

t = input();
t = int(t.strip())

for i in range(t):
    n = input()
    n = int(n.strip())

    commands = []
    for j in range(n):
        inputCommand = input()
        inputCommand = inputCommand.strip().split(' ')
        
        if inputCommand[0] == 'LEFT':
            command = -1
        elif inputCommand[0] == 'RIGHT':
            command = 1
        else:
            command = commands[int(inputCommand[-1])-1]
        commands.append(command)

    print(sum(commands))
