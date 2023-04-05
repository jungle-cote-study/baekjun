import sys
sort_arr= []
def search(data,n):
    if n == 1:
        return data[0][0]
    new_arr = [[]for _  in range(n//2)]
    for i in range(0,n,2):
        for j in range(0,n,2):
            sort_arr.append(data[i][j])
            sort_arr.append(data[i][j+1])
            sort_arr.append(data[i+1][j])
            sort_arr.append(data[i+1][j+1])
            new_arr[i//2].append(sorted(sort_arr,reverse=True)[1])
            sort_arr.clear()

    return search(new_arr, n//2)
    
data = []
n = int(sys.stdin.readline())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

print(search(data,n))
