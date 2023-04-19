import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline
# N, K = map(int,input().split())

# hanoi = [[]for _ in range(N+1)]
# hanoi[1].append([1,3])
# # hanoi[2].append([1,2])
# # hanoi[2].append([1,3])
# # hanoi[2].append([2,3])


# def hanoi_K(N):
#     if N<=1:
#         return
#     if N%2==0:
#         hanoi_K(N-1)
#         hanoi[N].append([1,3])
#         hanoi_K(N-1)
#     else:
#         hanoi_K(N-1)
#         hanoi[N].append([1,3])
#         hanoi_K(N-1)
# hanoi_K(N)
# print(hanoi)

# print(hanoi[N][K-1])


n,k = map(int,input().split())
def f(n, a,c,b):
  if n==0: return None
  
  if l[0]-2**(n-1)+1<=0:f(n-1,a,b,c)
  else: l[0]=l[0]-2**(n-1)+1
  l[0] -= 1
  if l[0]==0:
    print('%d %d' %(a,c))
    exit(0)
  if l[0]-2**(n-1)+1<=0:f(n-1,b,c,a)
#   else: l[0]=l[0]-2**(n-1)+1
l=[k]
f(n,1,3,2)