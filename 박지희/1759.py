import sys
     
L, C = map(int, sys.stdin.readline().split())

alphabet_list = list(map(str, sys.stdin.readline().split()))
alphabet_list.sort()
vowels = ['a', 'e', 'i', 'o', 'u'] # 모음들

# L개의 문자 만들기
# 최소 한 개의 모음
# 최소 두 개의 자음 
# 증가하는 순서로 배열
# 가능성 있는 암호 모두 구하기

# ['a', 'c', 'i', 's', 't', 'w']

result = []
def solv(idx, cnt, vowelsN, password): 
    
    print(idx, cnt, vowelsN, password)
    if cnt == 1: # 만약 남은 글자가 없으면?
        print(password)
        if 1 <= vowelsN and  2 <= L - vowelsN :
            result.append(password)
        return
    
    if alphabet_list[idx] in vowels: # 만약 모음이면? 
        vowelsN += 1
    
    for i in range(idx+1, C):
        if C - i  < cnt : # 만약 더 늦은 알파벳이 만들 숫자 만큼 없으면 못 만들어여
            break
        solv(i, cnt - 1, vowelsN, password + alphabet_list[i])
        
for idx in range(C):
    solv(idx, L, 0, alphabet_list[idx])

print(result)
