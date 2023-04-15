from sys import stdin
from collections import deque

n = int(stdin.readline())
board = []
for _ in range(n):
    input_line = stdin.readline().split()
    board.append([int(x) for x in input_line if x !="0"])

stack = [[board, 0]]
max_value = -0
while stack:
    now_board, cnt = stack.pop()
    cnt+=1
    new_board = []
    for i in range(n): # 왼
        j = 0
        tmp_row = deque()
        while j <= len(now_board[i])-1:
            if j == len(now_board[i])-1:
              tmp_row.append(now_board[i][j])
              break
            if now_board[i][j] == now_board[i][j+1]:
                tmp_row.append(now_board[i][j]*2)
                j+=2
            else:
                tmp_row.append(now_board[i][j]) 
                j+=1
        max_value = max(max_value, *tmp_row)
        new_board.append(list(tmp_row))
    stack.append([new_board, cnt])

    new_board = []
    for i in range(n): # 오   
        j = n-1
        tmp_row = deque()
        while j >=0:
            if j == 0:
              tmp_row.appendleft(now_board[i][j])
              break
            if now_board[i][j] == now_board[i][j-1]:
                tmp_row.appendleft(now_board[i][j]*2)
                j-=2
            else:
                tmp_row.appendleft(now_board[i][j]) 
                j-=1
        max_value = max(max_value, *tmp_row)
        new_board.append(list(tmp_row))
    stack.append([new_board, cnt])

    new_board = []
    for i in range(n): # 아
        col = []
        for j in range(n):
            col.append(now_board[j][i])
        j = 0
        tmp_board = []
        tmp_col = []
        while j <= len(col)-1:
            if j == len(col)-1:
              tmp_col.append(col[j])
              break
            if col[j] == col[j+1]:
                tmp_col.append(col[j]*2)
                j+=2
            else:
                tmp_col.append(col[j]) 
                j+=1
        tmp_board.append(tmp_col)
        max_value = max(max_value, *tmp_col)
    for j in range(n):
        tmp_row = []
        for k in range(n):
            tmp_row.append(tmp_board[k][j])
        new_board.append(list(tmp_col))
    stack.append([new_board, cnt])
    
    new_board = []
    for i in range(n): # 위
        col = []
        for j in range(n):
            col.append(now_board[j][i])
        j = n-1
        tmp_board = []
        tmp_col = deque()
        while j >=0:
            if j == 0:
              tmp_col.appendleft(col[j])
              break
            if col[j] == col[j-1]:
                tmp_col.appendleft(col[j]*2)
                j-=2
            else:
                tmp_col.appendleft(col[j]) 
                j-=1
        tmp_board.append(tmp_col)
        max_value = max(max_value, *tmp_col)
    for j in range(n):
        tmp_row = []
        for k in range(n):
            tmp_row.append(tmp_board[k][j])
        new_board.append(list(tmp_row))
    stack.append([new_board, cnt])
            
print(max_value)