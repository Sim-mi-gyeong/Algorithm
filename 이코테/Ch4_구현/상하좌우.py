# L: 왼쪽으로 한 칸 이동
# R: 오른쪽으로 한 칸 이동
# U: 위로 한 칸 이동
# D: 아래로 한 칸 이동
import time
start_time = time.time()

n = int(input())
path = list(input().split())

# 각 방향에 대한 딕셔너리 가능
L = [0, -1]
R = [0, 1]
U = [-1, 0]
D = [1, 0]
x, y = 1, 1

for i in range(len(path)):
    if path[i] == 'L':
        end_x = x + L[0]
        end_y = y + L[1]
    if path[i] == 'R':
        end_x = x + R[0]
        end_y = y + R[1]
    if path[i] == 'U':
        end_x = x + U[0]
        end_y = y + U[1]
    if path[i] == 'D':
        end_x = x + D[0]
        end_y = y + D[1]

    # 이동 후 좌표 먼저 확인 후 O / X 에 따라 이동 결정도 가능
    if end_x < 1 or end_y < 1 or end_x > n or end_y > n:
        continue

    x, y = end_x, end_y

end_time = time.time()
print(x, y) 
print('걸린 시간 : ', end_time)