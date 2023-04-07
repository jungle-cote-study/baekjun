import sys
input = sys.stdin.readline
n = int(input())
tops = list(map(int,input().split()))
answer= [0] * n
stack = []

for i in range(n):
    while stack:
        if tops[stack[-1][0]]<tops[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][0]+1 #인덱스를+1해서 저장~
            break
    stack.append((i,tops[i]))
    
print(*answer)


