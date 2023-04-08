import sys
import heapq
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
input = sys.stdin.readline
N, M, K = map(int,input().split())
beers = []
for _ in range(K):
    like , level = map(int,input().split())
    heapq.heappush(beers, [level, like])
print(beers)
beers_original = beers

while True:
    
    sum_ = 0
    max_level = 0
    for i in range(N):
        drink = heapq.heappop(beers)
        sum_ += drink[1]
        if drink[0] > max_level:
            max_level = drink[0]
    
    if sum_ >= M:
        print(max_level)
        break