import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
arr = [False]*N
cards = list()
for _ in range(N):
    cards.append(int(input()))

tmp = ''
permutation = set()

def permu(cnt):
    global tmp
    if cnt==K:
        permutation.add(tmp)
        return
    for i in range(N):
        if arr[i]!=True:
            tmp += str(cards[i])
            arr[i] = True
            permu(cnt+1)
            tmp = tmp[:-(len(str(cards[i])))]
            arr[i] = False

permu(0)
print(len(permutation))