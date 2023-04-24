import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline
# N = 원숭이 수
N = int(input().strip())


# 정답 참고
from collections import deque
cur = ['A']*N
check = [[False]*N for _ in range(N)]

ans = set()
def dq():
    q = deque([(0, N)])

    # 계속해서 반으로 쪼개면서 서로 상대팀이 되도록 한다.
    while q:
        for _ in range(len(q)):
            start, end = q.popleft()
            
            if end - start <= 1:
                continue
            
            mid = (start + end)//2
            
            for i in range(start, mid):
                cur[i] = 'A'
            for i in range(mid, end):
                cur[i] = 'B'
            q.append((start, mid))
            q.append((mid, end))
        ans.add(''.join(cur))
dq()

for a in ans:
    print(a)

for _ in range(7-len(ans)):
    print('A' + ('B' *(N-1)))
