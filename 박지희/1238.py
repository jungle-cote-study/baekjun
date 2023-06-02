# 첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.
import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())
load = [[] for _ in range(N + 1)]

def find_load(start_city):
    to_N = [sys.maxsize]  * (N + 1)
    que = []
    to_N[start_city] = 0
    heapq.heappush(que, [0, start_city]) # 시작 지점 넣기

    while(que):
        t, start = heapq.heappop(que) # 가장 시간이 짧게 걸리는 길 찾기
        # 해당 경로에서 갈 수 있는 길 찾기
        for end, time in load[start]:
            if to_N[end] > to_N[start] + time:
                to_N[end] = to_N[start] + time
                heapq.heappush(que, [to_N[end], end])
    return to_N

# 입력 받기
for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    load[start].append([end, time])
    
# 왕복 시간이 가장 오래 걸리는 사람 찾기
to_X = [sys.maxsize]  * (N + 1)
# 각 위치에서 X까지 가는 가장 가까운 경로 찾기
for i in range(N + 1):
    l = find_load(i)
    to_X[i] = l[X]

# 반대로 X에서 각 마을로 돌아가는 가장 가까운 경로 찾기
l = find_load(X)

# 두개의 각 경로의 값을 더해서 가장 큰 값을 찾기
result = 0
for i in range(1, N + 1):
    result = max(result, to_X[i] + l[i]) 
print(result)
