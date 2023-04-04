
import sys

n = int(sys.stdin.readline())

l = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

width =n
result = l[0:] ## 결과를 저장할 리스트
while width != 1:
    tamp = [[0] * (width//2) for _ in range(width//2)] ## 임시 저장할 리스트

    x = 0
    y = 0

    for i in range(0,width,2):
        y = 0
        for j in range(0,width,2):
            # 제일 작은 것 고르기
            m = max(result[i][j], result[i][j+1])
            m2 = min(result[i][j], result[i][j+1])
            if result[i+1][j] >= m :
                m2 = m
                m = result[i+1][j]
            elif result[i+1][j] >= m2 :
                m2 = result[i+1][j]
                
            if result[i+1][j+1] >= m :
                m2 = m
                m = result[i+1][j+1]
            elif result[i+1][j+1] >= m2 :
                m2 = result[i+1][j+1]
        
            tamp[x][y] = m2
            y += 1
        x+=1
            
    width = width// 2
    result = tamp[0:]
    
print(result[0][0])
