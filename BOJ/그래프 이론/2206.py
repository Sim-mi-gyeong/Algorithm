# 벽 부수고 이동하기

from collections import deque

n, m =map(int, input().split())
path = [list(list(map(int, input()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
path3D = []
for i in range(2):
    path3D.append(path)

# 1: 이동할 수 없는 벽
# 0: 이동 가능
# 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면,
# 벽을 한 개 까지 부수고 이동하여도 된다.
cnt = 0   # 벽을 부순 횟수 <= 1

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dx2, dy2 = [1, 0], [0, 1]
queue = deque([])

def bfs(x, y):
    global cnt
    queue.append([x, y])
    path[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            visited[nx][ny] = True    

            if path[nx][ny] == 0:
                print('(nx, ny) : ', (nx, ny))
                queue.append([nx, ny])
                path[nx][ny] = path[x][y] + 1
                break
            # 한 곳이라도 0이 있어서 넘어가면, 1이 있는 벽 부분을 넘어갈 조건 검사하지 않도록

            # 다음 위치가 벽이고, 벽을 부순 횟수가 0 회라면, (   ) 
            if path[nx][ny] == 1 and cnt == 0:  
                # path[nx][ny] == 1 인 곳을 한 번 넘어갔을 때 이동 거리가 더 짧아진다면, 
                for i in range(len(dx2)):
                    tx = nx + dx2[i]
                    ty = ny + dy2[i]

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue

                    if path[tx][ty] == 0:   # 벽을 부수고 넘어간 다음 지점이 또 벽이 아니라면
                        print('(tx, ty) : ', (tx, ty))
                        path[nx][ny] = path[x][y] + 1   # 벽을 한 번 부수고 
                        path[tx][ty] = path[nx][ny] + 1
                        queue.append([tx, ty])
                        cnt += 1
                        if cnt >= 1: break
                    elif path[tx][ty] == 1:
                        break

    return path[n-1][m-1]

if n == 1 and m == 1 and path[0][0] == 0:
    print(1)
    exit(0)
result = bfs(0, 0)

print('벽을 부순 횟수 : ', cnt)
print(path)

if result == 1 or result == 0 :   # 도착 지점이 방문처리 되어 있지 않으면
    print(-1)
    exit(0)
else: print(result)