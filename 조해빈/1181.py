import sys
input = sys.stdin.readline
N = int(input())
dicts = []
for _ in range(N):
    dicts.append(input().rstrip())

temp = set(dicts)
dicts = list(temp)

dicts.sort()
dicts.sort(key=lambda x:len(x))

for i in range(len(dicts)):
    print(dicts[i])