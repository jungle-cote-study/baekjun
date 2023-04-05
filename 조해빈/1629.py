import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
def recur(a, b, c):
    if b==1:
        return a*b%c
    else: 
        chunck = recur(a, b//2, c)
        if b%2==0:
            return (chunck * chunck) % c
        else:
            return (chunck * chunck * a) % c
print(recur(A, B, C))

# 시도하다가 안 된 풀이
# import sys
# input = sys.stdin.readline
# A, B, C = map(int, input().split())
# sum = 1
# def recur(a, b, c):
#     global sum
#     if b==1:
#         return a*b%c
#     if b%2==0:
#         sum *= recur(a, b//2, c)
#     else:
#         sum *= recur(a, b//2, c)*a
# recur(A, B, C)
# print(sum)