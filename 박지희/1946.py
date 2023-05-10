import sys


testcase_n = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(testcase_n):
    people_n = int(sys.stdin.readline())
    rank = []
    for _ in range(people_n):
        rank.append(list(map(int, sys.stdin.readline().split())))

    rank.sort()
    
    cnt = 0
    top_score = rank[0][1]
    
    for idx in range(people_n):
        check = True
        
        if rank[idx][1] <= top_score:
            cnt += 1 
            top_score = rank[idx][1]
            
            
    
    print(cnt)
    
    




