import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline
N = int(input().strip())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append([end , start])
meetings.sort(key=lambda x:x[1])
meetings.sort(key=lambda x:x[0])
end = 0
count = 0
que = deque()

for i in range(len(meetings)):
    que.append(meetings[i])
    end_meet , start_meet = que.popleft()
    if end <= start_meet:
        end = end_meet
        count += 1
print(count)