import sys
from collections import deque
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline
# bfs 하면서 한 덩어리씩 숫자 체크해서 해결..

N = int(input().strip())
map = deque([list(map(int, input().strip())) for i in range(N)])

dx = [-1, 1, 0 , 0]
dy = [ 0, 0, -1, 1]

# while(map):
