def move(no,x,y):
    if no > 1:
        print(no-1,x,6-x-y)
        move(no-1,x,6-x-y)
        
        # 현재 옮겨야할 블록의 갯수
        # x는 출발지 기둥
        # 6-x-y 빈 기둥의 번호를 구하는 수식
    
    print(x,y)
    if no > 1:
        print(no-1,x,6-x-y)
        move(no-1,6-x-y,y)



num = int(input())
print(2 ** num - 1) # 옮긴 횟수는 2^num-1이 된다
if num <= 20: # N이 20 이하인 입력이라는 전제조건
    move(num,1,3) # 모든 블럭은 1에 있으니까
