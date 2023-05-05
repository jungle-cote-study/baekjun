from sys import stdin

str1 = stdin.readline().rstrip()
str2 = stdin.readline().rstrip()

dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        dp[j][i] = dp[j-1][i-1]+1 if str2[j-1] == str1[i-1] else max(dp[j-1][i], dp[j][i-1])

print(dp[len(str2)][len(str1)])