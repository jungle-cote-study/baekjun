n = int(input())
arr = sorted(map(int, input().split()))  # 정렬된 용액들


def binary_search(s, target):
    global arr
    res = n
    start, end = s, n - 1

    while start <= end:
        mid = (start + end) // 2
 
        if arr[mid] >= target:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    return res


def solution():
    global arr
    v1, v2 = 0, 0
    best_sum = 1000000000
    for i in range(n):
        #이분탐색으로 최적의 용액 찾기
        res = binary_search(i + 1, -arr[i])
        
        #최적의 bestsum에 넣고 추후 더 나은값을 위해 if문, 각각 계산된 용액을 변수에 넣기
        print(i + 1 , res - 1 , n)
        if i + 1 <= res - 1 < n and abs(arr[i] + arr[res - 1]) < best_sum:
            best_sum = abs(arr[i] + arr[res - 1])
            v1, v2 = arr[i], arr[res - 1]

        #찾은 용액 확인
        if i + 1 <= res < n and abs(arr[i] + arr[res]) < best_sum:
            best_sum = abs(arr[i] + arr[res])
            v1, v2 = arr[i], arr[res]
    
    print(v1, v2) # 오름차순으로 출력


solution()