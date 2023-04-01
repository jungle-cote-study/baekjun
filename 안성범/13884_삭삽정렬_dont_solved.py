import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    K , N = map(int, input().split())
    dataset = list(map(int, input().split()))
    min_data = dataset.index(min(dataset))
    count = min_data
    while True:
        next_min_data=dataset[min_data:].index(min(dataset[min_data:]))
        count += next_min_data
        next_min_data = min_data
            
# 인덱스를 이용해서 다시 해야 할 듯