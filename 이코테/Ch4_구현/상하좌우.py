# L: 왼쪽으로 한 칸 이동
# R: 오른쪽으로 한 칸 이동
# U: 위로 한 칸 이동
# D: 아래로 한 칸 이동
import time
start_time = time.time()

n = int(input())
path = list(input().split())
print(path)

L = [0, -1]
R = [0, 1]
U = [-1, 0]
D = [1, 0]
start_x, start_y = 1, 1

for i in range(len(path)):
    
    if path[i] == 'L':
        start_x = start_x + L[0]
        start_y = start_y + L[1]
    if path[i] == 'R':
        start_x = start_x + R[0]
        start_y = start_y + R[1]
    if path[i] == 'U':
        start_x = start_x + U[0]
        start_y = start_y + U[1]
    if path[i] == 'D':
        start_x = start_x + D[0]
        start_y = start_y + D[1]
        
    if start_x < 1 or start_y < 1 or start_x > n or start_y > n:
        continue

    x, y = start_x, start_y
    print(x, y)

print(x, y)   # 1 4