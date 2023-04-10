from sys import stdin
import heapq

n = int(stdin.readline())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(stdin.readline()))

cnt = 0
while heapq:
    card1 = heapq.heappop(cards)
    if not len(cards):
        break
    card2 = heapq.heappop(cards)
    cnt += card1+card2
    heapq.heappush(cards, card1+card2)
print(cnt)
