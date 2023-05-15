import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

N , d, k, c = map(int, input().split())
belt = deque()
for _ in range(N):
    sushi = int(input().strip())
    belt.append(sushi)
for sushi_ in belt:
    tmp_sushi = []
    while (len(tmp_sushi)!=k):
        tmp = belt.popleft()
        tmp_sushi.append(tmp)
        belt.append(tmp)
    if (c in tmp_sushi):
        print(len(tmp_sushi)+1)