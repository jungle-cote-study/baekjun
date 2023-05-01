import sys

n =  int(sys.stdin.readline())

mongkeyTeamList = [''] * n

## 분할 정복으로 풀기
def divTeam(start, end):
    ## 종룔 조건은 내 옆에 한명까지 만났을 때!
    len = end - start
    mid = start + len//2
    if len == 1:
        return
    
    # 각 원숭이들을 반으로 나눠서 팀을 지정해주기
    for i in range(start, mid):
        mongkeyTeamList[i] += 'A'
    for i in range(mid, end):
        mongkeyTeamList[i] += 'B'
    
    ## 팀을 두개로 나눠서 각 팀은 A팀, B팀으로 설정해두기
    divTeam(start, mid) # 해당 팀에 팀 설정하기
    divTeam(mid, end) # 해당 팀에 팀 설정하기
    
divTeam(0, n)

for i in range(n):
    if len(mongkeyTeamList[i]) < 7:
        for _ in range(7-len(mongkeyTeamList[i])):
            if  i == 0:
                mongkeyTeamList[i] += 'A'
            else : 
                mongkeyTeamList[i] += 'B'
    # print(monkey)

for i in range(7):
    for j in range(n):
        print(mongkeyTeamList[j][i], end = "")
    print()
    
