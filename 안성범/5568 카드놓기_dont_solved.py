import sys
from itertools import permutations
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
input = sys.stdin.readline

n = int(input().strip())
k = int(input().strip())
cards = [int(input().strip())for _ in range(n)]

new = set(permutations(cards, k))
print(new)
answer = []
