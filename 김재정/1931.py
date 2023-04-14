# num = int(input())
# room = []
# check = 1
# for i in range(num):
#     time = list(map(int,input().split()))
#     room.append(time)

# result = sorted(room, key=lambda x: (x[1], x[0]))

# list_time=result[0][1]
# for i in range(1,num):
#     if list_time <= result[i][0]:
#         check +=1
#         list_time=result[i][1]

# print(check)
    

import sys
num = int(input())
result = []
arrs = []
check = []
for i in range(num):
    N,K = map(int, sys.stdin.readline().split())
    result.append([N,K])

result = sorted(result, key=lambda x: (x[1], x[0]))


check.append(result[0])
arrs.append(result[0])

for i in range(1,num):
    if check[0][1] <= result[i][0]:
        check.pop()
        check.append(result[i])
        arrs.append(result[i])


print(len(arrs))