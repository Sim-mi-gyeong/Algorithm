# 어른 상어
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

graph = []  # 모든 상어의 위치 정보 기록
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
# 모든 상어의 현재 방향 정보
directions = list(map(int, input().split()))

# 각 상어의 회전 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        tmp = list(map(int, input().split()))
        priorities[i].append(tmp)


# 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간] 저장하는 3차원 그래프
info_graph = [[[0] * 2 for _ in range(n)] for _ in range(n)]

# 특정 위치에서 이동 가능한 4가지 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 냄새 정보 업데이트
def update_smell():
    # 각 위치를 하나씩 확인하며
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하는 경우, 시간을 1 감소
            if info_graph[i][j][1] > 0:
                info_graph[i][j][1] -= 1
            # 상어가 존재(이동해온)하는 해당 위치의 냄새를 k 로 설정
            if graph[i][j] != 0:
                info_graph[i][j][0] = graph[i][j]
                info_graph[i][j][1] = k
                # info_graph[i][j] = [graph[i][j], k]


# 모든 상어를 이동시키는 함수
def move_shark():
    # 이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_graph = [[0] * n for _ in range(n)]
    # 각 위치를 하나씩 확인하며
    for x in range(n):
        for y in range(n):
            # 상어가 존재하는 경우 (이동 전 위치)
            if graph[x][y] != 0:
                curr_shark_num = graph[x][y]
                curr_direction = directions[curr_shark_num - 1]  # 현재 상어의 방향
                found = False
                # 일단 냄새가 존재하지 않는 곳이 있는지 확인
                for i in range(4):
                    next_direction = priorities[curr_shark_num - 1][curr_direction - 1][i]
                    nx = x + dx[next_direction - 1]
                    ny = y + dy[next_direction - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 냄새가 존재하지 않는 위치라면
                        if info_graph[nx][ny][1] == 0:
                            # 해당 상어의 방향을 이동시키기
                            directions[curr_shark_num - 1] = next_direction
                            # 상어 이동시키기 (만약, 이미 다른 상어가 있다면 -> 번호가 낮은 상어가 들어가도록)
                            if new_graph[nx][ny] == 0:
                                new_graph[nx][ny] = curr_shark_num
                            else:
                                new_graph[nx][ny] = min(new_graph[nx][ny], curr_shark_num)

                            found = True
                            break

                if found:
                    continue

                # 주변에 모두 냄새가 남아있는 경우, 자신의 냄새가 있는 곳으로 이동
                for i in range(4):
                    next_direction = priorities[curr_shark_num - 1][curr_direction - 1][i]
                    nx = x + dx[next_direction - 1]
                    ny = y + dy[next_direction - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 자신의 냄새가 있는 곳이라면
                        if info_graph[nx][ny][0] == curr_shark_num:
                            # 해당 상어의 방향 이동시키기
                            directions[curr_shark_num - 1] = next_direction
                            # 상어 이동시키기
                            new_graph[nx][ny] = curr_shark_num
                            break

    return new_graph


time = 0
while True:
    update_smell()  # 모든 위치의 냄새 업데이트 (초기 포함)
    new_graph = move_shark()  # 모든 상어 이동
    graph = new_graph  # 그래프 정보 업데이트
    time += 1

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    # 1000초가 지날 때까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break
