from sys import stdin
from itertools import permutations

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
operator = list(map(int, stdin.readline().split()))

op_seq = ['pl', 'mi', 'mul', 'div']
op_arr = []
for i in range(4):  # i는 연산자별 횟수
    for _ in range(operator[i]):
        op_arr.append(op_seq[i])

min_result = 10**10
max_result = -10*10

for comb in permutations(op_arr, sum(operator)):
    result = nums[0]
    for i in range(1, n):
        if comb[i-1] == 'pl':
            result += nums[i]
        elif comb[i-1] == 'mi':
            result -= nums[i]
        elif comb[i-1] == 'mul':
            result *= nums[i]
        else:
            result = result // nums[i] if result > 0 else -(-result//nums[i])
    min_result = min(min_result, result)
    max_result = max(max_result, result)

print(max_result, min_result, sep='\n')
