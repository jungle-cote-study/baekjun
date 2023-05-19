import sys

N, d, k, c = map(int, sys.stdin.readline().split())

sushi_list = [int(sys.stdin.readline()) for _ in range(N)]

check_list = [0] * 3001 # 먹은 초밥의 종류를 체크할 리스트
check_cupon = 1 # 쿠폰 초밥의 먹은 여부를 체크할 변수

window_start = 0 # 윈도우의 시작 인덱스
result = 0 # 결과

# 초기 윈도우의 초밥 종류와 쿠폰 초밥의 먹은 여부를 체크한다.
check_num = 0

for i in range(k):
    if check_list[sushi_list[i]] == 0:
        check_num += 1
    
    check_list[sushi_list[i]] += 1
    
    if sushi_list[i] == c:
        check_cupon = 0
        
# 슬라이딩 윈도우 알고리즘을 적용한다
for window_end in range(k, N+k):
    # 현재 윈도우의 마지막 초밥을 체크한다
    new_sushi = sushi_list[window_end % N]
    # 현재 윈도우의 첫 번째 초밥을 체크한다
    delete_sushi = sushi_list[window_start % N]
    
    # 현재 윈도우에서 빠진 초밥을 체크하고 체크 리스트에서 제거한다
    check_list[delete_sushi] -= 1
    if check_list[delete_sushi] == 0: # 만약 빠진 초밥이 중복이 아니었다면
        
        check_num -= 1  # 최종 결과 값에서 하나 뺀다.
        if delete_sushi == c : # 쿠폰이랑 같은 초밥이었는지 확인한다.
            check_cupon = 1 # 같은 초밥이었다면 쿠폰이 의미 있어지니까 1로 만들어줌
    
    # 현재 윈도우에 추가된 초밥을 체크하고 체크 리스트에 추가한다
    if check_list[new_sushi] == 0:
        check_num += 1
        if new_sushi == c : # 추가될 초밥이 쿠폰이랑 같은 초밥인지 확인한다
            check_cupon = 0 # 만약 쿠폰이랑 같은 초밥이면 의미가 없어지니까 1로 만든다.
    check_list[new_sushi] += 1
    
    result = max(result, check_num + check_cupon)

    # 다음 윈도우의 첫 번째 초밥 인덱스를 설정한다
    window_start += 1

print(result)

    
            
