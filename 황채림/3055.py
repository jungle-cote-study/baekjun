from sys import stdin
from collections import deque
import copy

r, c = map(int, stdin.readline().split())
map = []
for _ in range(r):
    map.append(list(stdin.readline()))

q = deque()
q.append([0, map])
dir = [[-1,0], [1,0],[0,-1],[0,1]]
answer = -1

while q:
    cnt, map = q.popleft()
    for i in range(r):
        for j in range(c):
            if map[i][j] == '*':
                for d in dir:
                    if 0 <= i+d[0] <= r-1 and 0 <= j + d[1] <= c-1 and map[i+d[0]][j+d[1]] == '.':
                        map[i+d[0]][j+d[1]] = '*'
            elif map[i][j] == 'S':
                hedgehog = [i,j]

    for d in dir:
        if 0 <= i+d[0] <= r-1 and 0 <= j + d[1] <= c-1:
            if map[i+d[0]][j+d[1]] == '.':
                newmap = copy.deepcopy()
                newmap[i][j] == 'x'
                newmap[i+d[0]][j+d[1]] = 'S'
                q.append([cnt+1, newmap])
            elif map[i+d[0]][j+d[1]] == 'D':
                answer = cnt+1
                break
    
    if answer != -1:
        break

if answer == -1:
    print('KAKTUS')
else:
    print(answer)
