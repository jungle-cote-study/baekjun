import sys
import heapq
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

N = int(input().strip())

cards = [int(input().strip())for _ in range(N)]
heapq.heapify(cards)
count = 0
while len(cards)!=1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    c = a + b
    count += c
    heapq.heappush(cards, c)

print(count)