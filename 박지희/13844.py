# 삭삽 정렬
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    testCaseN, N = map(int,sys.stdin.readline().split())
    
    l = list(map(int,sys.stdin.readline().split()))
    sortL = l[0:]
    sortL.sort()
    
    max1 = l[0]
    count = 0
    result = 0
    # print(sortL)
    
    # while count < len(l)-1 :
    count = 0
    for i in range(0,len(l)):
        # print(l[i], sortL[count])
        if l[i] > sortL[count]:
            result += 1
        else : count+= 1

    print(testCaseN,result)
