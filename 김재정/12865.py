n, w = map(int, input().split())

dp = [[0] * (w+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight, value = map(int, input().split())
    for j in range(w+1):
        if weight > j:  # 배낭의 용량보다 물건의 무게가 더 큰 경우
            dp[i][j] = dp[i-1][j]
        else:  # 물건을 선택하는 경우와 선택하지 않는 경우 중 더 큰 값 선택
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[n][w])