# 1629 : 곱셈

import sys

A ,B, C= map(int, sys.stdin.readline().split())

def power(A, B):
    if(B == 1) :
        return A % C
     
    result = power(A, B//2) 
    if( B % 2  == 1) :
        return (result * result * A) % C
    else : 
        return result * result % C
        


print(power(A,B))
