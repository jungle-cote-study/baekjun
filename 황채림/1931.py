from sys import stdin
import heapq

n = int(stdin.readline())

meeting=[]
for _ in range(n):
    start, end = map(int, stdin.readline().split())
    heapq.heappush(meeting, [end, start])

answer = 0
endtime = -1
for i in range(n):
    m = heapq.heappop(meeting)
    if m[1]>=endtime:
        answer+=1
        endtime = m[0]

print(answer)
