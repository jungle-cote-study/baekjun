import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

N = int(input().strip())
liquid = sorted(list(map(int,input().split())))
print(liquid)
answer = [0]*2
cur = 10**10
start_ptr = 0
end_ptr = N-1



while start_ptr < end_ptr:
    if cur == 0:
        break
    mid_ptr = (start_ptr+end_ptr)//2    
    sub = abs(liquid[start_ptr]+liquid[end_ptr])
    if sub < cur:
        answer[0] = liquid[start_ptr]
        answer[1] = liquid[end_ptr]
        cur = sub            
    else:
        end_ptr -= 1
        start_ptr += 1
print(*answer)