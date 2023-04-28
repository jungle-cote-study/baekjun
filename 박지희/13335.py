import sys
from collections import deque
# 트럭의 수 n, 다리의 길이 w, 다리의 최대하중 l
n, w, l = map(int, sys.stdin.readline().split())
# 트럭의 무게
trucks = deque(list(map(int, sys.stdin.readline().split())))

# 다리 상태
bridge = deque([0]*w)

# 흐른 시간
time = 0

# 유닛 시간이 흐를 때마다 계산을 한다.
while(trucks):
    # 지금 다리의 무게
    
    bridge.popleft()
    total_weight = sum(bridge)
    # 만약 대기 트럭이 들어와도 되면(들어와도 최대 하중을 안넘으면)
    if total_weight + trucks[0] <= l:
        # print(time, "초에", trucks[0],"이 들어옴")
        bridge.append(trucks.popleft())
    else :
        bridge.append(0) 
    time +=1
    # print(time, bridge)

print(time + w)
