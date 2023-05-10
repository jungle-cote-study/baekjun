import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

N, M = map(int, input().split())
max_list = [[]for i in range(N+1)]
min_list = [[] for i in range(N+1)]
count = 0

for i in range(M):
    a, b = map(int, input().split())
    max_list[a].append(b)
    min_list[b].append(a)





for i in range(N+1):
    if max_list[i] >= (M+1)/2 or min_list[i] >= (N+1)/2:
        count += 1

print(max_list)
print(min_list)