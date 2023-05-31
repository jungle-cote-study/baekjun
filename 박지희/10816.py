import sys

plus_count = [0] * 10000001
minus_count = [0] * 10000001

N = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split()))

for card in cards:
    if 0 <card :
        plus_count[card] += 1
    else : 
        minus_count[card] += 1
        
N2 = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

for number in numbers:
    if 0 <number :
        print(plus_count[number], end=" ")
    else : 
        print(minus_count[number], end=" ")
     
