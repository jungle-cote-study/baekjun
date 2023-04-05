from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()

left = 0
right = n-1
diff = 10**10
answer = [10**7, 10**7]
while left < right:
    if abs(arr[right]+arr[left]) < abs(diff):
        diff = arr[right]+arr[left]
        answer[0] = arr[left]
        answer[1] = arr[right]
    if arr[right]+arr[left] > 0:
        right -= 1
    elif arr[right]+arr[left] < 0:
        left += 1
    else:
        break

print(answer[0], answer[1])
