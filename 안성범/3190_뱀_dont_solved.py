import sys
from collections import deque
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())
apples = [list(map(int,input().split()))for _ in range(K)]
T = int(input().strip())
event = [input().split() for _ in range(T)]
gragh = [[0]*N for _ in range(N)]
for apple in apples:
    gragh[apple[0]-1][apple[1]-1] = 1

direction_x = (0, 1, 0, -1)
direction_y = (1, 0, -1, 0)
t = 0
snake = deque()
snake.append([0,0])
while True:

    x, y = snake.popleft()
    dx = x + direction_x[]
    dy = y + direction_y[]
    if 0< x <N and 0<y<N and 0<dx<N and 0<dy<N :
        snake.append([dx,dy])
        if gragh[dx][dy] != 1:
            snake.popleft()
    t += 1


    for i in range(T):
        if t == event[i][0]:
            dx = x + direction_x[i]
            dy = y + direction_y[i]
