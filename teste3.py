from random import randint
import math

n = 50
m = 100000
variavel = 0
total = 0

for c in range(0, m):
    for d in range(0, n):
        randomnum = randint(0, 1)
        if randomnum == 0:
           randomnum = -1
        variavel += randomnum
    if variavel < 0:
        variavel *= (-1)
    total += variavel
    variavel = 0

total = total/m
pi = (2*n)/total**2
print(pi)
