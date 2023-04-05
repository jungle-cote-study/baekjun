# 단어 정렬
import sys

n = int(sys.stdin.readline())
words = set()
[words.add(sys.stdin.readline().strip()) for _ in range(n)]
words = list(words)
words.sort()
words.sort(key = len)
[print(word) for word in words]
