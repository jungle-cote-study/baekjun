import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    result = 1
    min_score = 0
    member_list = []
    for j in range(N):
        a, b = map(int, input().split())
        member_list.append([a, b])
    member_list.sort(key=lambda x:x[0])
    min_score = member_list[0][1]
    for k in range(1, len(member_list)):
        if (min_score > member_list[k][1]):
            result += 1
            min_score = member_list[k][1]
    print(result)