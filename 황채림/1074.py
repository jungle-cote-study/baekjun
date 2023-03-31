from sys import stdin
n, r, c = map(int, stdin.readline().split())


def z(s_x, s_y, k):
    if k == 1:
        return 1
    answer = 0
    quard = [[s_x, s_x+k//2-1, s_y, s_y+k//2-1],  # x축 시작/끝, y축 시작/끝
             [s_x+k//2, s_x+k-1, s_y, s_y+k//2-1],
             [s_x, s_x+k//2-1, s_y+k//2, s_y+k-1],
             [s_x+k//2, s_x+k-1, s_y+k//2, s_y+k-1]]
    for i in range(4):
        if quard[i][2] <= r <= quard[i][3] and quard[i][0] <= c <= quard[i][1]:
            answer += z(quard[i][0], quard[i][2], k//2)
            break
        else:
            answer += (k//2)**2
    return answer


print(z(0, 0, 2**n)-1)
