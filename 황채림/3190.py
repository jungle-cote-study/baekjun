from sys import stdin
from collections import deque

n = int(stdin.readline())
k = int(stdin.readline())
apple = []
for _ in range(k):
    apple.append(tuple(map(int, stdin.readline().split())))
l = int(stdin.readline())
turn = deque()
for _ in range(l):
    input_turn = stdin.readline().split()
    turn.append((int(input_turn[0]), input_turn[1]))

time = 0
directions = {0: (1, 0), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
dir_idx = 0
snake = deque()
snake.append((1, 1))


def make_turn(turn_dir, now_dir):
    if turn_dir == 'D':
        if now_dir != 3:
            return now_dir+1
        else:
            return 0
    else:
        if now_dir != 0:
            return now_dir - 1
        else:
            return 3


while True:
    if turn[0][0] == time:
        dir_idx = make_turn(turn[0][1], dir_idx)
        turn.popleft()

    head_x = snake[0][0]
    head_y = snake[0][1]
    head_x += directions[dir_idx][0]
    head_y += directions[dir_idx][1]
    new_head = (head_x, head_y)

    if new_head in snake or head_x < 0 or head_x > n-1 or head_y < 0 or head_y > n-1:
        break

    snake.appendleft(new_head)
    if not new_head in apple:
        snake.pop()
    time += 1

print(time)
