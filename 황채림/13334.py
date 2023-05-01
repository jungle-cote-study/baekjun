from sys import stdin
import heapq

n = int(stdin.readline())
temp = []
stop = []
for _ in range(n):
    t = list(map(int, stdin.readline().split()))
    # 범위 안에 포함되기 시작하는 건 l_end >= 끝값일 때니까 끝값 기준으로 정렬
    # 사실상 끝값과 시작값을 따로 보는 것
    if t[0] < t[1]:
        t = [t[1], t[0]]
    temp.append(t)
    stop.append(t[0])
    stop.append(t[1])
d = int(stdin.readline())
stop = sorted(list(set(stop)))

commute = []
for t in temp:
    if t[0]-t[1] <= d:
        heapq.heappush(commute,t)

answer = 0
in_l = []
for l_start in stop:
    l_end = l_start+d

    while commute and commute[0][0] <= l_end:
        heapq.heappush(in_l,heapq.heappop(commute)[1])
    while in_l and in_l[0] < l_start:
        heapq.heappop(in_l)
    answer = max(answer, len(in_l))

    
print(answer)
