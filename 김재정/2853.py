N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

boat = 0
for i in range(1, N):
    if arr[i] == 0:
        continue
    a = arr[i] - arr[0]
    temp = 1
    for j in range(1, N):
        if arr[j] == 0:
            continue
        if arr[j] % a == 1:
            temp += a
            arr[j] = 0
    if temp != 1:
        boat += 1

print(boat)