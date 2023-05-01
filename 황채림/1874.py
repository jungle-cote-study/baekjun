from sys import stdin

n = int(stdin.readline().rstrip())
target = []
for _ in range(n):
    target.append(int(stdin.readline()))

stack = []
cnt = 0
answer = []

for i in range(n):
    stack.append(i+1)
    answer.append('+')
    if i+1 == target[cnt]:
        while len(stack)>0 and stack[-1] == target[cnt]:
            stack.pop()
            answer.append('-')
            cnt+=1

if len(stack) > 0:
    print("")
else:
    print(*answer, sep='\n')

