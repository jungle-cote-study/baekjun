from sys import stdin
import sys
sys.setrecursionlimit(10**8)

a, b, c = map(int, stdin.readline().split())
answer = 1


def pow_num(a, b, c):
    if b == 1:
        return a % c
    if b == 2:
        return a**2 % c
    else:
        if b % 2 == 0:
            return pow_num(a, b//2, c)**2 % c
        else:
            return (pow_num(a, b//2, c)**2*a) % c


print(pow_num(a, b, c))
