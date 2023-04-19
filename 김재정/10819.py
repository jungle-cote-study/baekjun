import itertools

n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0
for p in itertools.permutations(a):
    sum = 0
    for i in range(n-1):
        print(p[i], p[i+1], abs(p[i] - p[i+1]))
        sum += abs(p[i] - p[i+1])
    ans = max(ans, sum)

print(ans)