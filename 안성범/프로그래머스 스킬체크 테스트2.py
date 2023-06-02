def solution(nums):
    answer = []
    for pocket in nums:
        if pocket in answer:
            continue
        else:
            answer.append(pocket)
            
    maximum = len(nums)/2
    if len(answer) > maximum:
        return maximum
    else:
        return len(answer)