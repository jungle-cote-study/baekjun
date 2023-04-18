n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_value = 0

# 방향 인덱스: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방향 이동 함수
def move(direction):
    if direction == 0:  # 상
        for j in range(n):
            for i in range(1, n):
                if board[i][j]:
                    x = i
                    while x > 0 and board[x-1][j] == 0:
                        board[x-1][j] = board[x][j]
                        board[x][j] = 0
                        x -= 1
                    if x > 0 and board[x-1][j] == board[x][j]:
                        board[x-1][j] *= 2
                        board[x][j] = 0
    elif direction == 1:  # 하
        for j in range(n):
            for i in range(n-2, -1, -1):
                if board[i][j]:
                    x = i
                    while x < n-1 and board[x+1][j] == 0:
                        board[x+1][j] = board[x][j]
                        board[x][j] = 0
                        x += 1
                    if x < n-1 and board[x+1][j] == board[x][j]:
                        board[x+1][j] *= 2
                        board[x][j] = 0
    elif direction == 2:  # 좌
        for i in range(n):
            for j in range(1, n):
                if board[i][j]:
                    y = j
                    while y > 0 and board[i][y-1] == 0:
                        board[i][y-1] = board[i][y]
                        board[i][y] = 0
                        y -= 1
                    if y > 0 and board[i][y-1] == board[i][y]:
                        board[i][y-1] *= 2
                        board[i][y] = 0
    elif direction == 3:  # 우
        for i in range(n):
            for j in range(n-2, -1, -1):
                if board[i][j]:
                    y = j
                    while y < n-1 and board[i][y+1] == 0:
                        board[i][y+1] = board[i][y]
                        board[i][y] = 0
                        y += 1
                    if y < n-1 and board[i][y+1] == board[i][y]:
                        board[i][y+1] *= 2
                        board[i][y] = 0



    
def check():
    for i in range(4):
        temp_board = [row[:] for row in board] # 보드 복사
        move(i)  # 방향 이동
        max_value = max(max_value, max(board[i]))
        board = [row[:] for row in temp_board]  # 보드 되돌리기


check()
# 최대 블록 값 출력
print(max_value)
