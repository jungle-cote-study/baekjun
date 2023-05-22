import sys

N = int(sys.stdin.readline())

start = int(sys.stdin.readline())

num_list = []

for _ in range(N - 1):
    num = int(sys.stdin.readline())
    check = True
    for i in num_list : 
        if (num - 1) % i == 0 :
            check = False
            break
    if check :
        num_list.append(num-1)
            
print(len(num_list))
    
    
