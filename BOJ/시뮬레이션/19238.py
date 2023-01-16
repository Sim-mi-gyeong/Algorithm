# 스타트 택시

from collections import deque
import sys

input = sys.stdin.readline

n, m, puel = map(int, input().split())
graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(n):
        if tmp[j] == 1:
            graph[i][j] = -1

init_x, init_y = map(int, input().split())
init_x = init_x - 1
init_y = init_y - 1

peoples_dic = dict()
peoples_check_dic = dict()
for i in range(1, m + 1):
    x, y, nx, ny = map(int, input().split())
    peoples_dic[i] = [x - 1, y - 1, nx - 1, ny - 1]
    peoples_check_dic[i] = 0
    graph[x - 1][y - 1] = i

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_bfs(startX, startY):
    q = deque()
    visited = [[0] * n for _ in range(n)]

    visited[startX][startY] = 1
    q.append((startX, startY, 0))

    enable_people = []
    while q:
        x, y, dist = q.popleft()
        if graph[x][y] != 0 and graph[x][y] != -1:
            people_num = graph[x][y]
            if peoples_check_dic[people_num] != 1:
                enable_people.append((people_num, dist))
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != -1:
                visited[nx][ny] = 1
                q.append((nx, ny, dist + 1))

    return enable_people


def choose_people(startX, startY):
    global puel
    enable_people = find_bfs(startX, startY)
    if len(enable_people) == 0:
        return -1

    enable_people_loc = []
    for tmp_people_num, tmp_dist in enable_people:
        enable_people_loc.append(
            (
                tmp_people_num,
                peoples_dic[tmp_people_num][0],
                peoples_dic[tmp_people_num][1],
                tmp_dist,
            )
        )

    enable_people_loc = sorted(enable_people_loc, key=lambda x: (x[3], x[1], x[2]))
    target_people = enable_people_loc[0]
    target_people_num, target_people_dist = target_people[0], target_people[3]

    if puel - target_people_dist < 0:
        # print(-1)
        return -1

    puel -= target_people_dist
    return target_people_num


INF = int(1e9)


def move(people_num):
    people = peoples_dic[people_num]
    startX, startY, endX, endY = people[0], people[1], people[2], people[3]

    q = deque()
    visited = [[0] * n for _ in range(n)]

    visited[startX][startY] = 1
    q.append((startX, startY, 0))

    while q:
        x, y, dist = q.popleft()
        if (x, y) == (endX, endY):
            return dist
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != -1:
                visited[nx][ny] = 1
                q.append((nx, ny, dist + 1))

    return INF


def check():
    cnt = 0
    flag = False
    for k, v in peoples_check_dic.items():
        if v == 1:
            cnt += 1
    if m == cnt:
        flag = True
    return flag


def solve():
    global puel
    startX, startY = init_x, init_y
    while True:
        if check():
            print(puel)
            break

        tmp_result = choose_people(startX, startY)
        if tmp_result == -1:
            print(-1)
            break
        else:
            people_num = tmp_result
            dist = move(people_num)
            if dist == INF:
                print(-1)
                break
            if puel - dist < 0:
                print(-1)
                break
            else:
                peoples_check_dic[people_num] = 1
                puel -= dist
                puel += dist * 2

                people_start_x, people_start_y, people_end_x, people_end_y = (
                    peoples_dic[people_num][0],
                    peoples_dic[people_num][1],
                    peoples_dic[people_num][2],
                    peoples_dic[people_num][3],
                )
                graph[people_start_x][people_start_y] = 0

                startX, startY = people_end_x, people_end_y


solve()
