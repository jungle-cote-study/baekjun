from sys import stdin

n,m = map(int, stdin.readline().split())
pair = []
for _ in range(m):
    pair.append(list(map(int, stdin.readline().split())))

pair.sort(key=lambda x:x[1])
pair.sort(key=lambda x:x[0])
sequence = []
stack = []

while len(stack) < n:
    p = pair.pop()
    if p[0] in sequence:
        # sequence.append(p[1])
        # dfs 결과를 스택에 저장
    elif p[1] in sequence:
        # sequence.insert(0, p[0])
    else:
        # sequence.append()
