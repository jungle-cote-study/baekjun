import sys
N = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

index = N // k
arr = []

for i in range(0,N,index):
    arr = c[i:i+index]
    arr.sort()
    print(*arr, end =" ")
    
    
    
    
