import sys
from itertools import permutations

n,k = int(sys.stdin.readline()), int(sys.stdin.readline())

card = [int(input()) for _ in range(n)]

result = set()
for i in list(permutations(card,k)):
    result.add("".join(list(map(str,i))))


print(len(result))