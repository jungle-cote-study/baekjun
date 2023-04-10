from sys import stdin
import heapq

n, m, k, = list(map(int, stdin.readline().split()))
beer = []
for _ in range(k):
    favor, alcohol = map(int, stdin.readline().split())
    heapq.heappush(beer, (alcohol, favor))

liver = 2**31
satisfaction = 0
days = 0
result = []
for _ in range(k):
    days += 1
    if days > n:
        satisfaction -= heapq.heappop(result)
        days -= 1

    alcohol, favor = heapq.heappop(beer)
    heapq.heappush(result, favor)
    liver = alcohol
    satisfaction += favor
    if satisfaction > m:
        break


if satisfaction < m:
    print(-1)
else:
    print(liver)

# n일동안 하루 하나씩 n개 마셔야 함
# 맥주 n개 합 >=m
# 그때의 도수 최소합
# 안되면 -1
#
# =>n개 합은 m이상이기만 하면 되고 최소ㅎ일 필요는 없다
# =>도수가 최소인게 더 중요
