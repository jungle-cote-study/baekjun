def hanoiPrint(n, a, b):
  if n>0:
    hanoiPrint(n-1, a, (6-a-b))
    print(f"{a} {b}")
    hanoiPrint(n-1, (6-a-b), b)

h = int(input())
moveSum = 2**h-1
print(moveSum)
if(h <= 20):
  hanoiPrint(h, 1, 3)
