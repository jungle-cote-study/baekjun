import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline
def hanoi(N, a, b, c):
    if N==0:
        return
    hanoi(N-1,a,c,b)
    print(a, c)
    hanoi(N-1,b,a,c)
N = int(input().strip())

if N<=20:
    print(2**N-1)
    hanoi(N,1,2,3)
else:
    print(2**N-1)