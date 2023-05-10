from sys import stdin
from itertools import combinations

l, c = map(int, stdin.readline().split())
alp = stdin.readline().split()
vowel = ["a", "i", "e", "o", "u"]

moeum = []
jaeum = []
for i in alp:
    if i in vowel:
        moeum.append(i)
    else:
        jaeum.append(i)

moeum.sort()
jaeum.sort()

answer = []
for i in range(1, len(moeum) + 1):
    if l - i < 2:
        break
    moeum_combi = list(combinations(moeum, i))
    jaeum_combi = list(combinations(jaeum, l - i))

    for m in moeum_combi:
        for j in jaeum_combi:
            answer.append("".join((sorted(m + j))))

answer.sort()
print(*answer, sep="\n")
