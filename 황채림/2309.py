from sys import stdin
from itertools import permutations

height = []
for _ in range(9):
    height.append(int(stdin.readline()))

perm = permutations(height, 7)
for case in perm:
    if sum(case) == 100:
        print(*sorted(list(case)), sep='\n')
        break
