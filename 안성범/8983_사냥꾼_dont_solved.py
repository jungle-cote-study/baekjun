import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline
# M : 사대의 수, N : 동물의 수, L : 사정거리
M , N , L = map(int, input().split())

hunter_x = sorted(list(map(int, input().split())))
animal_list = [list(map(int, input().split())) for _ in range(N)]
animal_list.sort(key=lambda x:x[0])
count = 0
start = 0
end = len(hunter_x)

while animal_list:
    mid = (start+end)//2
    target = animal_list.pop()
    if target[1] > L:
        continue
    while True:
        if target[0] < hunter_x:
            mid = 

print(hunter_x)
print(animal_list)
