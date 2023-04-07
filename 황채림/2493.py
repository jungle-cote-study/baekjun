from sys import stdin
from collections import deque

n = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
answer = []
stack = deque()
for i in range(n):
    flag = True
    while stack:
        if towers[stack[-1]] > towers[i]:
            answer.append(stack[-1]+1)
            flag = False
            break
        else:
            stack.pop()
    if flag:
        answer.append(0)
    stack.append(i)

print(*answer)
