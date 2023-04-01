# 삭삽 정렬
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    testCaseN, N = map(int,sys.stdin.readline().split())
    l = []
    for i in range(N//10):
        l += list(map(int,sys.stdin.readline().split()))
    if N % 10:
        l += (list(map(int,sys.stdin.readline().split())))
    sortL = l[0:]
    sortL.sort()
    count = 0
    result = 0
    
    count = 0
    for i in range(0,len(l)):
        if l[i] > sortL[count]:
            result += 1
        else : count+= 1

    print(testCaseN,result)
