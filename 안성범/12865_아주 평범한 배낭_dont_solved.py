import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline
N , K = map(int, input().split())
backpack = [[0, 0]]
for _ in range(N):
    backpack.append(list(map(int,input().split())))
dp = [[0]*(K+1)for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = backpack[i][0], backpack[i][1]
    dp[0][weight] = value
for i in range(1, N+1):
    weight, value = backpack[i][0], backpack[i][1]
    for j in range(1,K+1):
        if j >= weight:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
print(dp[-1][-1])