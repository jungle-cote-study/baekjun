from sys import stdin

n = int(stdin.readline())
house = []
for _ in range(n):
    house.append(list(map(int,list(stdin.readline().rstrip()))))

dir = [[-1, 0], [0,-1], [1,0], [0, 1]]
complex = []
for i in range(n):
    for j in range(n):
        dir_flag = False
        for d in dir:
            if dir_flag:
                break
            if 0 <= i+d[0] < n and 0 <= j+d[1] < n and house[i+d[0]][j+d[1]] == 1:
                already_flag = False
                for c in complex:
                    if [i+d[0], j+d[1]] in c[0]:
                        c[0].append([i,j])
                        c[1] +=1
                        dir_flag = True
                        break
        if house[i+d[0]][j+d[1]] == 1 and not dir_flag:
            complex.append([[i,j], 1])

answer = []
for d in complex:
    answer.append[c[1]]

answer.sort()
print(sum(answer))
print(answer)