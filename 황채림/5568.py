from sys import stdin

n = int(stdin.readline())
k = int(stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(stdin.readline()))


def permutations(arr, k):
    if k == 1:
        return [[x] for x in arr]
    answer = []
    for i in range(len(arr)):
        rest = arr[:i]+arr[i+1:]
        result = permutations(rest, k-1)
        answer.extend([x+[arr[i]] for x in result])
    return answer


result = permutations(nums, k)
answer = []
for n in result:
    n = map(str, n)
    answer.append(''.join(n))
print(len(set(answer)))
