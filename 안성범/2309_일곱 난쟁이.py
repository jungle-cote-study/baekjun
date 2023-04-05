import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt','w')
dwarf_height = [int(input().strip())for _ in range(9)]
print(dwarf_height)
gue_dwarf = list(combinations(dwarf_height, 7))
print(gue_dwarf)
for i in range(len(gue_dwarf)):
    if sum(gue_dwarf[i]) == 100:
        answer = sorted(gue_dwarf[i])
        break
for dwarf in answer:
    print(dwarf)