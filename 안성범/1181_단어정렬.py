import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

N = int(input().strip())
word_list = []
for i in range(N):
    word = input().strip()
    if not word in word_list:
        word_list.append(word)
word_list.sort()
word_list.sort(key= lambda x:len(x))

for i in range(len(word_list)):
    print(word_list[i])
    