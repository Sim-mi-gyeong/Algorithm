# 벽 부수고 이동하기

from collections import deque

n, m = map(int, input().split())
path = [list(list(map(int, input()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque([])

def bfs(): 
    queue.append([0, 0, 0])
    visited[0][0][0] = 1

    while queue:
        # cnt : 벽을 부쉈는지 여부를 같이 큐에 넣고, 빼고를 할 수 있어야 함
        x, y, cnt = queue.popleft()

        # 큐에서 꺼낸 위치가 마지막 위치일 경우, 리턴
        if x == n-1 and y == m-1: 
            return visited[x][y][cnt]

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 만나지 않은 경우, 방문하지 않은 경우!! -> 방문 체크도 해야함
                if path[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    queue.append([nx, ny, cnt])

                # 벽을 만나고, 벽을 부술 수 있는 경우
                elif path[nx][ny] == 1 and cnt == 0:
                    # 한 층 위로 올라가면서, 해당 위치에서 벽을 부순 것을 확인 가능
                    visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                    queue.append([nx, ny, cnt + 1])

                # 벽을 만났지만 벽을 부술 수 없는 경우

    # 위에서 처리되지 못한 경우, 
    # 예를 들어 마지막 위치까지 큐에 넣고 빼내지 못한 경우(도착 지점이 방문처리 되어 있지 않으면), 불가능의 return -1
    return -1

print(bfs())