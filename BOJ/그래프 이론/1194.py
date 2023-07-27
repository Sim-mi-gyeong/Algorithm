# 달이 차오른다, 가자.


from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().rstrip().split())

# 같은 타입의 열쇠 / 문 은 여러 개 있을 수 있고,
# 문에 대응하는 열쇠가 없을 수도 있음
# '0' : 민식이의 현재 위치 / '1' : 출구 (여러 개 가능)

# 민식이가 미로를 탈출하는데 드는 이동 횟수의 최솟값
def bfs(startX, startY):
    q = deque()
    visited = [[0] * m for _ in range(n)]

    visited[startX][startY] = 1
    q.append((startX, startY, 0))

    while q:
        print("큐 상태 : ", q)
        x, y, cnt = q.popleft()
        print("(x, y, cnt) : ", (x, y, cnt))
        if graph[x][y] == "1":
            return cnt

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == ".":
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))

                elif graph[nx][ny].isalpha() and graph[nx][ny].islower():
                    key[ord(graph[nx][ny]) - ord("a")] = 1
                    visited = [[0] * m for _ in range(n)]
                    print("열쇠를 찾은 후 방문배열 초기화 상태 : ", visited)
                    print("큐 초기화 전 q : ", q)

                    q = deque()
                    print("큐 초기화 후 q : ", q)

                    graph[nx][ny] = "."
                    visited[nx][ny] = 1
                    print("열쇠를 찾은 경우 (nx, ny, cnt + 1): ", (nx, ny, cnt + 1))
                    q.append((nx, ny, cnt + 1))
                    print("큐에 열쇠를 찾은 위치 추가 후 q : ", q)

                elif graph[nx][ny].isalpha() and graph[nx][ny].isupper():
                    if key[ord(graph[nx][ny]) - ord("A")]:  # 열쇠가 있는 경우
                        graph[nx][ny] = "."  # 문을 열어 빈공간 처리
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt + 1))
                elif graph[nx][ny] == "1":
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))

    return -1


graph = []
for i in range(n):
    tmp = list(input().rstrip())
    graph.append(tmp)
    key = [0] * 6
    for j in range(m):
        if tmp[j] == "0":
            startX, startY = i, j
            graph[i][j] = "."  # 빈 공간 처리
        # elif tmp[j].isalpha() and tmp[j].islower():
        #     key[ord(tmp[j]) - ord("a")] = 1

ans = bfs(startX, startY)
print(ans)
