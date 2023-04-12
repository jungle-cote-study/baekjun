# 1715 : 카드 정렬하기

import sys, heapq

n = int(sys.stdin.readline())

cards = []

for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

result = 0

while(len(cards) > 1):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards) 
    result += card1 + card2
    heapq.heappush(cards, card1 + card2)
    
print(result)
