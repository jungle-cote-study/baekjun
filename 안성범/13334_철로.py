import sys
import heapq
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

N = int(input().strip())
human_list = []
for i in range(N):
    a, b = map(int, input().split())
    if b < a:
        human_list.append([b, a])
    else:
        human_list.append([a, b])
human_list.sort(key=lambda x:x[1])
length_road = int(input().strip())
able = []
for human in human_list:
    if (human[1]-human[0] <= length_road):
        able.append(human)
able_two = sorted(able)
ans = 0
while able_two:
    one = heapq.heappop(able_two)
    tmp_ans = 0
    for human in able:
        if (one!=human and human[0] >= one[0] and human[1] <= one[0]+length_road):
            tmp_ans += 1
    ans = max(tmp_ans , ans)
print(ans+1)