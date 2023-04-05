import sys
from math import gcd
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')
input = sys.stdin.readline

N = int(input().strip()) -2
routine = list(map(int, input().split()))
print(routine)
_lcm = routine[0]
for planet in routine[1:]:
    _lcm = int(_lcm*planet / gcd(_lcm, planet))
print(_lcm)
# print(N)
# for i in range(N-2):
#     fir_planet = routine[i]
#     sec_planet = routine[i+1]
#     gcd_ = gcd(routine[i], routine[i+1])
#     lcm = routine[i]/gcd_*routine[i+1]


# def gcd(a, b):
#     if a < b:
#         a , b = b, a
#     while True:
#         r = a%b
#         if r == 0:
#             break
#         a, b = b, r
#     return b
