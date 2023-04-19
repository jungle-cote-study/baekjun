from sys import stdin

n = int(stdin.readline())
cnt = 0
result = []

def hanoii(k, a, c):
    global cnt
    cnt+=1
    if k==1:
        result.append(f"{a} {c}")
        return
    hanoii(k-1, a, 6-a-c)
    result.append(f"{a} {c}")
    hanoii(k-1, 6-a-c, c)

if n>20:
    print(2**n-1)
else:
    hanoii(n, 1, 3)
    print(cnt)
    print(*result, sep="\n")
    
