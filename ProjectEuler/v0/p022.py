#!/bin/python3

def countNameScore(name):
    score = 0
    for alpha in name:
        score += (ord(alpha) - ord('A') + 1)
    return score

with open('p022_names.txt', 'r') as f:
    names = sorted(f.readline().replace('"', '').strip().split(','))
    cnt, score = 1, 0
    
    for name in names:
        score += cnt * countNameScore(name)
        cnt += 1

    print(score)
