import random

data = [0] * 9
for i in range(0,9): #순서대로 입력 받아 리스트에 저장
  data[i] = int(input())

result = 0

while result != 100:
  real = random.sample(data,7)
  result = sum(real)

real = sorted(real)

for i in real:
  print(i)