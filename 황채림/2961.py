from sys import stdin
from itertools import combinations
from functools import reduce

n = int(stdin.readline())

taste = []
for _ in range(n):
    taste.append(list(map(int,stdin.readline().split())))

answer = 10**9
for i in range(1, n+1):
    combi = combinations(taste, i)
    for c in combi:
        s = [x[0] for x in c]
        b = [x[1] for x in c]
        answer = min(answer, abs(reduce(lambda x,y: x*y, s, 1)-sum(b)))
        
print(answer)