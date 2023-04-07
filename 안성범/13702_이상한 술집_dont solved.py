import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

# N , K = map(int, input().split())   # N : 막걸리 개수, K : 인원 수
# mak = [int(input().strip())for _ in range(N)]
# print(mak)
# mak_avg = sum(mak)//K
# print(mak_avg)
# start = 0
# end = max(mak)
    
# while start <= end:
#     mid = mak_avg
#     sum_k = 0
#     for i in range(N):
#         sum_k += mak[i]/mid
#     if sum_k >= K: