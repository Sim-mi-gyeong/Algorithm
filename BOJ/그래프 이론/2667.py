# 단지번호붙이기
# 단지 수 출력 -> 각 단지에 속하는 집의 수를 오름차순 정렬
from collections import deque

n = int(input())
house = [list(map(int, input())) for _ in range(n)]
cnt = []   # len(cnt): 단지 개수
h = 0   # 단지 개수, 집이 있는 곳 개수 Count

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# def bfs(x, y):
#     if x < 0 or y < 0 or  x >= n or y >= n:
#         return False
#     start = house[x][y]
#     queue = deque([start])

#     while queue:
#         v = queue.popleft()

#         if v == 1:
#             house[x][y] = 0
#             queue.append(v)
        
#         for i in range(len(dx)):
#             nx = x + dx[i]
#             ny = y + dy[i]

def dfs(x, y):
    global h
    if x < 0 or y < 0 or  x >= n or y >= n:
        return False

    if house[x][y] == 1:
        h += 1
        house[x][y] = 0   
        
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True   # True를 반환하는 기준은, 단지가 생성되는 기준 -> dfs가 재귀적으로 수행되는 것이 우선
    
for i in range(n):
    for j in range(n):
        if dfs(i, j):             
            cnt.append(h)
            h=0
            
print(len(cnt))
for i in sorted(cnt): print(i)