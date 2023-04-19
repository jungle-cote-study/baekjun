import sys
import itertools

n = int(sys.stdin.readline())
datas =list(map(int, sys.stdin.readline().split()))

permutation = itertools.permutations(datas, n)
# 각 순열을 돌면서 최대 차이를 찾는다. 
maxN = 0
for per in permutation:
    before = per[0]
    sum = 0
    # print(before, end= " ")
    for num in per:
        sum += abs(before-num) 
        before = num
        # print(before, end= " ")
        # print("sum = " , sum, end=",")
        
    maxN= max(sum, maxN)
print(maxN)
