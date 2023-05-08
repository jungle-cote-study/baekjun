from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    score = []
    for _ in range(n):
        score.append(list(map(int, stdin.readline().split())))

    score.sort(key=lambda x: x[0])

    answer = 0

    for i in range(n - 1, -1, -1):
        flag = 0
        for j in range(i - 1, -1, -1):
            if score[j][1] < score[i][1]:
                flag = 1
                break
        if not flag:
            answer += 1

    print(answer)
