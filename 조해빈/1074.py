import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())
cnt = 0

def conq(n, x, y):
    global cnt

    while n>0:
        n-=1
        quarter = 2**n

        if x<quarter and y<quarter:   # 1st square
            cnt += quarter*quarter*0
        elif x<quarter and y>quarter: # 2nd square
            cnt += quarter*quarter*1
            y -= quarter
        elif x>quarter and y<quarter: # 3rd square
            cnt += quarter*quarter*2
            x -= quarter
        else:                         # 4th square
            cnt += quarter*quarter*3
            x -= quarter
            y -= quarter

    return cnt

result = conq(N, r, c)
print(result)