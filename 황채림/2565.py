from sys import stdin
from collections import deque

t = int(stdin.readline())
lines = []
for _ in range(t):
    lines.append(list(map(int, stdin.readline().split())))
lines.sort(key=lambda x: x[0])

memo = deque()
for l in lines:
    m_len = len(memo)
    if m_len == 0:
        memo.append((1, l[1]))
    else:
        for _ in range(m_len):
            m = memo.popleft()
            if l[1] > m[1]:
                memo.append((m[0] + 1, l[1]))
            else:
                memo.append((1, l[1]))
            memo.append(m)

max_lines = -1
for i in memo:
    max_lines = max(max_lines, i[0])

print(t - max_lines)
