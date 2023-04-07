import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

A , B, C = map(int, input().split())
answer = 1
def multi(a, b, c):
    global answer
    while b>1:
        if b %2 == 0:
            answer*= multi(a, b//2, c)%c*multi(a,b//2, c)%c
        else:
            answer*= multi(a,b//2,c)%c*multi(a,b-b//2,c)%c
    return (a*b)%c

print(multi(A,B,C))