import sys
input = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for _ in range(input)]

data_set = set(data)
data = list(data_set)
data.sort()
data.sort(key=len)

for i in data:
    print(i)
