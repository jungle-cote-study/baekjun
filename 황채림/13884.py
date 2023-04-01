from sys import stdin
# from collections import deque

p = int(stdin.readline())
for _ in range(p):
    k, n = map(int, stdin.readline().split())
    numbers = list(map(int, stdin.readline().split()))
    sorted_num = sorted(numbers)
    cnt = 0
    i = 0

    while True:
        flag = numbers[i] > numbers[i+1]
        if True:
            popped = numbers[i]
            numbers = [x for x in numbers if x != popped] + [popped]
            cnt += 1
        if i == n-cnt-1:
            if numbers[:n-cnt] == sorted_num[:n-cnt]:
                break
            else:
                i = 0
                continue
        if False:
            i += 1
    print(k, cnt)
