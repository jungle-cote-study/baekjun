
import sys
N = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))
l.sort()
def f(a, b):
    for i in range(max(a,b), a*b + 1):
        if i % a == 0 and i % b == 0:
            return i
# print(l)
result = l[0]
for i in range(1,len(l)):
    if (l[i] % result == 0):
        result = l[i]
        # print(result)
    else : result =  f(result,l[i])
    
print(result)
    
