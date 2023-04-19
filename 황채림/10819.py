from sys import stdin

# 풀이 1
from itertools import permutations

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))

result = permutations(num, n)
answer = 0
for arr in result:
    arr = list(arr)
    cnt = 0
    for i in range(n-1):
        cnt += abs(arr[i]-arr[i-1])
    answer = max(answer, cnt)

print(answer)

# 풀이2
# 95퍼에서 틀림? 이전 풀이랑 비교해 봐야 할 듯
# from collections import deque

# n = int(stdin.readline())
# num = list(map(int, stdin.readline().split()))

# num.sort()
# small = num[:n//2]
# small.reverse()
# big = num[n//2:] 
# arr = deque()
# flag = True
# while len(small) > 0 and len(big) > 0:
#     if flag:
#         arr.append(big.pop())
#         arr.appendleft(small.pop())
#     else:
#         arr.appendleft(big.pop())
#         arr.append(small.pop())
#     flag = not flag
    
# if len(small) > 0:
#     if flag:
#         arr.appendleft(small.pop())
#     else:
#         arr.append(small.pop())
# elif len(big) > 0:
#     if flag:
#         arr.append(big.pop())
#     else:
#         arr.appendleft(big.pop())
        
# answer = 0
# for i in range(n-1):
#     answer += abs(arr[i]-arr[i+1])
    
# print(answer)