def solution(arr):
    ans = [arr[0]]
    for i in range(len(arr)-1):
        if (arr[i+1] == arr[i]):
            continue
        else: 
            ans.append(arr[i+1])
    return ans

print(solution([1,1,3,3,0,1,1]))
