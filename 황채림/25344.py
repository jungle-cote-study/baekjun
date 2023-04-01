from sys import stdin

n = int(stdin.readline())
planet = list(map(int, stdin.readline().split()))
planet.sort()

answer = 1
for i in planet:
    if answer % i == 0:
        continue
    else:
