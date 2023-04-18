from sys import stdin
from collections import deque

n, k = map(int,stdin.readline().split())

memo = deque()
cnt = 0
before_move = 3

# def hanoii(n, k, before_move, using_tower):
#     if k <= n/2-1:
#         memo.appendleft((k, 5-before_move))
#         if k == 1:
#             return
#         hanoii(k-1, 5-before_move)
#     else:
#         memo.appendleft((k, ))

def hanoii(k, target, cannot_move):
    memo.appendleft((k, target))
          
    
    
memo.append((n, 3))
hanoii(n-1, 3)
print(*memo[k-1], sep=' ')