import sys
import heapq

V, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(V + 1)]

start_v = int(sys.stdin.readline())

## 입력 받아서 방향 그래프 만들기 O(E)
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v,w])
dist_list = [sys.maxsize] * (V+1)  

que = [] 
heapq.heappush(que, [0, start_v])
dist_list[start_v] = 0 # 시작 지점의 비용은 0이다. 

while(que):
    # 가장 비용이 작은 노드 탐색 
    min_dist, min_node = heapq.heappop(que)
    # 가장 비용이 작은 노드에서 갈 수 있는 방향 탐색하기
    for v, d in graph[min_node]:
        if dist_list[v] > dist_list[min_node] + d:
            dist_list[v] = dist_list[min_node] + d
            heapq.heappush(que, [d, v])
        
for d in dist_list[1:]: 
    if d == sys.maxsize:
        print("INF")
    else :
        print(d)
