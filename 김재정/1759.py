import sys
from itertools import combinations
input = sys.stdin.readline

l,c = map(int,input().split())
data = list(input().split())
vowel = {"a","e","i","o","u"}
data.sort()

def function(password):
    except_vowel_password = set(password) - vowel
    intersection_vowel_password = set(password) & vowel
    flag = 0
    if len(except_vowel_password) < 2 or len(intersection_vowel_password) <1:
        flag = 1
    return flag

for comb in combinations(data,l):
    if function(comb) == 0:
        print(''.join(comb))