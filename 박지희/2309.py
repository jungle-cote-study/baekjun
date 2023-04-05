# 2309 : 일곱 난이
import sys
from itertools import permutations

people = [int(sys.stdin.readline()) for _ in range(9)]

results = permutations(people, 7)
# print(results)

for result in results:
    result = list(result)
    if sum(result) == 100:
        result.sort()
        [print(d) for d in result]
        break
