# 2470 : 두 용액
import sys
input = sys.stdin.readline


N = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)


left = 0
right = N-1
value = numbers[left] + numbers[right]
pick_numbers = [numbers[left], numbers[right]]

while left < right:
    temp = numbers[left] + numbers[right]
    if abs(value) > abs(temp):
        value = temp
        pick_numbers = [numbers[left], numbers[right]]
        if value == 0:
            break

    if temp < 0:
        left += 1
    else:
        right -= 1

print(*pick_numbers)
