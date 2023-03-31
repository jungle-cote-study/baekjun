import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
input = sys.stdin.readline

N , r, c = map(int, input().split())
# gragh = [[0]*(2**N)for _ in range(2**N)]
# print(gragh)
answer = 0
def Z(depth, a, b):
    global answer , N
    if a == 0 and b == 0:
        return
    if a >= 2**(N/2-depth) and b >= 2**(N/2-depth):
        position = 4
    elif a >= 2**(N/2-depth) and b < 2**(N/2-depth):
        position = 3
    elif a < 2**(N/2-depth) and b >= 2**(N/2-depth):
        position = 2
    elif a < 2**(N/2-depth) and b < 2**(N/2-depth):
        position = 1
    
    answer += (position-1)*(2**(N-depth*2))
    Z(depth+1, a//2, b//2)


Z(0, r,c)
print(answer)