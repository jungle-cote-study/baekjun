import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline
N = int(input().strip())
inf = int(1e9)


houses = []
for _ in range(N):
    red, green, blue = map(int, input().split())
    houses.append([red, green, blue])

visited_check = [0]*N
dp = [inf]*N

print(houses)
