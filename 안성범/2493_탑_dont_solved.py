import sys
from collections import deque
sys.stdin =open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

N = int(input().strip())
tower = list(map(int, input().split()))

stack = deque()
stack.append(tower[0])
result = [0]
max_tower = [tower[0]]
for i in range(N+1):
    if stack[i] <= stack[i+1]:
        result.append(0)
        stack.append(stack[i+1])
        stack.popleft()
    else:
        result.append(stack[i])
        