# 1074 : Z
# 오답 : 시간 초과
import sys

N, r, c = map(int, sys.stdin.readline().split())

count = 0
find = False
def Z(start, width):
    # 각 행렬을 4등분으로 나눈 다음 Z로 탐색한다. 
    global find
    if find : return
    if width == 1:
        global count 
        if start[0] == r and start[1]==c :
            print(count)
            find = True
            return 
        count += 1
        return 0 
    Z(start,width//2)
    Z([start[0], start[1] + width//2], width//2)
    Z([start[0] + width//2, start[1]], width//2)
    Z([start[0] + width//2, start[1] + width//2], width//2)
    
    
    
Z([0,0],2 ** N)
# print(count)
