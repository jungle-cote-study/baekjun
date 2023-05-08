import sys


testcase_n = int(sys.stdin.readline())

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
        
        # 2차 시험 순위가 상위권자들 보다 더 낮으면
        if rank[idx][1] > top_score:
            continue
        cnt += 1 
        top_score = rank[idx][1]
            
            
    
    print(cnt)
    
    




