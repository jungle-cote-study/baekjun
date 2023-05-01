import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

N = int(input().strip())
num_list = []
for i in range(1, N+1):
    num_list.append(i)
ans_list = []
for i in range(N):
    ans_list.append(int(input().strip()))
    
print(ans_list)
print(num_list)