from sys import stdin

n = int(stdin.readline())
words = {}
max_length = 0
for _ in range(n):
    input_word = stdin.readline().rstrip()
    word_len = len(input_word)
    if not words.get(word_len):
        words[word_len] = set()
    words[word_len].add(input_word)
    max_length = max(max_length, word_len)

for i in range(1, max_length+1):
    if words.get(i):
        print(*sorted(list(words[i])), sep='\n')
