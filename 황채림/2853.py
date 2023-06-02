from sys import stdin

n = int(stdin.readline())
happy = []
for _ in range(n):
    happy.append(int(stdin.readline())) 

answer = 0
while len(happy) > 1:
    answer +=1
    diff = happy[1]-happy[0]
    b = happy[0]
    tmp = [b]
    break_flag = False
    while not break_flag and b <= happy[-1]:
        if b in happy:
            tmp.append(b)
            b += diff
        else :
            tmp = []
            break_flag = True
            answer -=1
    
    happy = [x for x in happy if x not in tmp]

if len(happy) == 1:
    print(answer+1)
else:
    print(answer)

