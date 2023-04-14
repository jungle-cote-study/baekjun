import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline
N = int(input().strip())
M = int(input().strip())
buses = []
for i in range(M):
    a, b, cost = map(int, input().split())
    buses.append([cost, a, b])

visited_check = [[0]*(N+1)]