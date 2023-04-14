from sys import stdin

n,k = map(int, stdin.readline().split())
stuff = []
for _ in range(n):
    stuff.append(list(map(int, stdin.readline().split())))

max_value = -1
memo = {}
stack = []
stack.append([[], stuff, k])
while stack:
    picked, left_stuff, left_weight = stack.pop()
    for i in range(len(left_stuff)):
        pick = left_stuff[i]
        new_left_stuff = left_stuff[:i]+left_stuff[i+1]
        memo[picked+[pick]] = memo[picked]+pick[0] if memo.get(picked) else pick[0]

        if left_stuff and left_weight >= min(new_left_stuff)[1]:
          stack.append([picked+[pick],new_left_stuff, left_weight-pick[1]])

print(max(memo, key=memo.get))
    