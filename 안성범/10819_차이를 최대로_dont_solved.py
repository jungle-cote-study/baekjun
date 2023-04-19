import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline
def sum_abs(a, b):
    new_num = abs(new_list[a] - new_list[b])
    return new_num
N = int(input().strip())
number_list = list(map(int, input().split()))
number_list.sort()
real_sum = 0

print(number_list)

new_list = []
new_list.append(number_list[(N-1)//2])
new_list.append(number_list[-1])
new_list.append(number_list[0])
new_list.append(number_list[-2])
new_list.append(number_list[1])
new_list.append(number_list[-3])
print(new_list)
for i in range(N-1):
    real_sum += sum_abs(new_list[i],new_list[i+1])
print(real_sum)