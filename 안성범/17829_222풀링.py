import sys
from collections import deque
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

N = int(input().strip())
gragh = [list(map(int, input().split()))for _ in range(N)]
def conq(length):
    global gragh
    if N!=1:
        new_gragh = [[0]*(length//2)for _ in range(length//2)]

        for i in range(0, length, 2):
            for j in range(0, length, 2):
                num_list = []
                num_list.append(gragh[i][j])
                num_list.append(gragh[i][j+1])
                num_list.append(gragh[i+1][j])
                num_list.append(gragh[i+1][j+1])
                num_list.sort()
                new_gragh[i//2][j//2] = num_list[-2]
        gragh = new_gragh
        conq(N//2)
    else:
        return new_gragh[-1][-1]
conq(N)