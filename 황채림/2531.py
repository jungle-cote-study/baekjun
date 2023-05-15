from sys import stdin

n,d,k,c = map(int, stdin.readline().split())

sushi = []
for _ in range(n):
    sushi.append(int(stdin.readline()))

answer = 0
for i in range(n):
    if i+k <= n:
      picked = sushi[i:i+k]
    else:
      picked = sushi[i:] + sushi[:k-(n-i)]
    
    kind_n = 0
    tmp = [0 for _ in range(d)]
    flag = False
    for pl in picked:
      if not pl in tmp:
          kind_n += 1
          tmp.append(kind_n)
      if pl == c:
          flag = True
      
    if not flag:
      kind_n += 1

    answer = max(kind_n, answer)
    if kind_n == k+1:
      break

print(answer)