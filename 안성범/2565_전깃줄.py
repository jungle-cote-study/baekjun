import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

height = int(input().strip())
edges = []
for i in range(height):
    a , b = map(int, input().split())    
    edges.append([abs(a-b),a, b])
edges.sort()
flag = 0
print(edges)
while flag != 1:
    delete_one = edges.pop()
    for edge in edges:
        if (delete_one[1] > edge[1] and delete_one[2] < edge[2]) or (delete_one[1] < edge[1] and delete_one[1] > edge[1]):
            flag = 1
            break
print(height - len(edges))        
    