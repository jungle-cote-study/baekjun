import sys

N = int(sys.stdin.readline())
result = [[''] * N for _ in range(7)]

def func(depth, start, end):
    if depth == 7:
        return

    mid = (start + end) // 2

    for i in range(start, mid):
        result[depth][i] = 'A'

    for i in range(mid, end):
        result[depth][i] = 'B'

    func(depth + 1, start, mid)
    func(depth + 1, mid, end)

func(0, 0, N)

for i in range(7):
    if 'A' not in result[i]:
        result[i][0] = 'A'
    print(''.join(result[i]))
