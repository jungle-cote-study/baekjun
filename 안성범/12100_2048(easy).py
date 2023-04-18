import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

N = int(input().strip())
gragh = [[0]*(N)for _ in range(N)]
print(gragh)
count = 0
for _ in range(4):
    direction_y = [-1, 1, 0, 0]
    direction_x = [0, 0 , -1, 1]
    
def move(direction_y, dirction_x):
    