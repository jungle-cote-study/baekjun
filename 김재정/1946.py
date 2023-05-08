import sys
num = int(input())

for _ in range(num):
    people = int(input())
    result = []
    arr = []

    for i in range(people):
        N,K = map(int, sys.stdin.readline().split())
        result.append([N,K])

    result.sort(key = lambda x : x[0])

    temp = result[0][1]
    arr.append(result[0])

    for i in range(1,people):
        if temp > result[i][1]:
            arr.append(result[i])
            temp = result[i][1]

        
        
    print(len(arr))