import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')
input = sys.stdin.readline
N = int(input().strip())
nums = list(map(int,input().split()))
a, b, c, d = map(int,input().split())
total =0
max_answer = 0
min_answer = 0
total = nums[0]
def equation(depth, total, plus, minus, multiply, devide):
    
    maximum_val = 0
    minimum_val = 10**12

    while depth != N:
        if plus != 0:
            total += nums[depth]
            equation(depth+1, total, plus-1, minus, multiply, devide)
        elif minus != 0:
            total -= nums[depth]
            equation(depth+1, total, plus, minus-1, multiply, devide)
        elif multiply != 0:
            total *= nums[depth]
            equation(depth+1, total, plus, minus, multiply-1, devide)
        elif devide != 0:
            total //= nums[depth]
            equation(depth+1,total, plus, minus, multiply, devide-1)
    max_answer = max(maximum_val, total)
    min_answer = min(minimum_val, total)

equation(1,total, a, b, c, d)
print(max_answer, min_answer)

# 정답코드
# import sys
# input = sys.stdin.readline
# N = int(input().strip())
# num = list(map(int, input().split()))
# operator_num = list(map(int, input().split()))

# maximum = -1e9
# minimum = 1e9


# def operator(depth, total, plus, minus, multiply, divide):
#     global maximum, minimum
#     if depth == N:
#         maximum = max(total, maximum)
#         minimum = min(total, minimum)
#         return
#     if plus != 0:
#         operator(depth+1 , total+num[depth], plus-1, minus, multiply, divide)
#     if minus != 0:
#         operator(depth+1, total-num[depth], plus, minus-1, multiply, divide)
#     if multiply != 0:
#         operator(depth+1, total*num[depth], plus, minus, multiply-1, divide)
#     if divide != 0:
#         operator(depth+1 ,int(total/num[depth]), plus, minus, multiply, divide-1)


# operator(1, num[0] ,operator_num[0], operator_num[1], operator_num[2], operator_num[3])
# print(maximum)
# print(minimum)