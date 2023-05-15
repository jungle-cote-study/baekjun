import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline
# N : 재료의 개수
N = int(input().strip())
tastes = [list(map(int, input().split()))for _ in range(N)]
print(tastes)
ans = 1e9
for taste in tastes:
    if (taste[1]-taste[0] < ans):
        ans = taste[1]-taste[0]
while True:
    food = []
    