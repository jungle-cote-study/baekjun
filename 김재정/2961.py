#2961

from itertools import combinations

n = int(input())
s_arr= []
b_arr= []

for _ in range(n):
    s, b = map(int, input().split())
    s_arr.append(s)
    b_arr.append(b)

min_diff = float('inf')

for i in range(1, n + 1):
    for comb in combinations(range(n), i):
        s_sum = 1
        b_sum = 0
        for j in comb:
            s_sum *= s_arr[j]
            b_sum += b_arr[j]
        min_diff = min(min_diff, abs(s_sum - b_sum))

print(min_diff)
