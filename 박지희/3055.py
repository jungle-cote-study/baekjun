import sys
from collections import deque
# 티떱숲의 지도는 R행 C열로 이루어져 있다. 
# 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다. 
# 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

R, C = map(int, sys.stdin.readline().split())
tw_map = []

for _ in range(R):
    tw_map.append(list(sys.stdin.readline().strip()))
    

que = deque()
now_positions = deque()
goal = [0,0]

# 고슴도치 위치랑 물 위치 찾기
for r in range(R):
    for c in range(C):
        # 지금 고슴도치 위치
        if tw_map[r][c] == "S":
            tw_map[r][c]= "."
            deque.append(now_positions, [r,c])         
        # 목표 지점 위치
        elif tw_map[r][c] == "D":
            goal = [r,c]
        # 물 위치
        elif tw_map[r][c] == "*":
            deque.append(que, [r,c])         
# 물 증가 함수 
# BFS로 물 증가 시키기
def next_water():
        # 상하좌우 탐색 후 물 넘치기
    global que
    next_q = deque()
    while(que):
        r, c = deque.popleft(que)
        if r+1 < R and tw_map[r+1][c] =='.':
            tw_map[r+1][c] = "*"
            deque.append(next_q, [r+1,c])
        if r-1 >= 0 and tw_map[r-1][c] =='.':
            tw_map[r-1][c] = "*"
            deque.append(next_q, [r-1,c])
        if c+1 < C and tw_map[r][c+1] =='.':
            tw_map[r][c+1] = "*"
            deque.append(next_q, [r,c+1])
        if c-1 >= 0 and tw_map[r][c-1] =='.':
            tw_map[r][c-1] = "*"
            deque.append(next_q, [r,c-1])
    que = next_q
    print("water", que)
# 고슴도치가 갈 수 있는 길 찾기
def move_position():
    global now_positions
    next_q = deque()
    while(now_positions):
        r, c = deque.popleft(now_positions)
        for x in [1, -1, 0, 0]:
            for y in [0, 0, 1, -1]:
                if 0 <= r + x < R and 0 <= c < C:
                    if r + x == goal[0] and c + y == goal[1]:
                        return True
                    deque.append(next_q, [r + x,c + y])
    now_positions = next_q
    print("positions" , now_positions, )
    print("goal" , goal, )
    return False
    
# 물이 가득 차거나, 고슴도치가 목표에 도착할 때까지 반복하기
result = "KAKTUS"
time = 1
while(que):
    next_water()
    print(">>>>>", time)
    [print(tw) for tw in tw_map]
    time += 1
    if move_position():
        result = time
        break
    
    
print(result)
    
