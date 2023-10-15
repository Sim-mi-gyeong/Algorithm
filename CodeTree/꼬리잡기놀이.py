import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def detect_line(startX, startY):
    teammates = [(startX, startY)]
    x, y = startX, startY

    while graph[x][y] != 3:
        for d in range(len(dx)):
            nx = x + dx[d]
            ny = y + dy[d]
    
            if not in_range(nx, ny):
                continue
            if len(teammates) >= 2 and (nx, ny) == teammates[-2]:
                continue

            if graph[x][y] == 1 and graph[nx][ny] == 3:
                continue
            if graph[nx][ny] not in [2, 3]:
                continue
            x, y = nx, ny
            break

        teammates.append((x, y))

    return teammates


def move_one_team(teammates):

    x, y = teammates[0]

    for d in range(len(dx)):
        nx = x + dx[d]
        ny = y + dy[d]
        if not in_range(nx, ny):
            continue

        if graph[nx][ny] not in [3, 4]:
            continue

    new_coords = []
    for teammate in teammates:
        cx, cy = teammate
        new_coords.append((nx, ny))
        nx, ny = cx, ny
        graph[cx][cy] = 4

    for idx, (x, y) in enumerate(new_coords):
        if idx == 0:
            graph[x][y] = 1
        elif idx == len(new_coords) - 1:
            graph[x][y] = 3
        else:
            graph[x][y] = 2

def detect_whole_teams():
    teams = []
    # 1. 모든 머리를 찾고
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                # 2. 각 팀을 찾는 함수
                teams.append(detect_line(i, j))
    return teams


def move_whole_teams():

    teams = detect_whole_teams()

    for teammates in teams:
        move_one_team(teammates)

def throw_ball(round_num):
    round_num %= n * 4

    if round_num < n:
        x1, y1 = round_num, 0
        x2, y2 = round_num, n
        pass
    # 위에서 아래로
    elif round_num < n * 2:
        x1, y1 = n - 1, round_num - n
        x2, y2 = -1, round_num - n
        pass
    # 오른쪽에서 왼쪽으로
    elif round_num < n * 3:
        x1, y1 = (3 * n - 1) - round_num, n - 1
        x2, y2 = (3 * n - 1) - round_num, -1
    else:
        x1, y1 = 0, (4 * n - 1) - round_num
        x2, y2 = n, (4 * n - 1) - round_num

    dx, dy = (x2 - x1) // n, (y2 - y1) // n
    x, y = x1, y1

    while (x, y) != (x2, y2):
        if graph[x][y] not in [0, 4]:
            return x, y

        x, y = x + dx, y + dy

    return None 


def calculate(x, y):
    teams = detect_whole_teams()
    for teammates in teams:
        for teammate in teammates:
            for idx, teammate in enumerate(teammates, 1):
                if teammate == (x, y):
        
                    x1, y1 = teammates[0]
                    x2, y2 = teammates[-1]
                    graph[x1][y1], graph[x2][y2] = graph[x2][y2], graph[x1][y1]
                    return idx * idx

ans = 0
for round_num in range(k):

    move_whole_teams()

    tmp = throw_ball(round_num)
    if tmp == None:
        continue
    x, y = tmp

    ans += calculate(x, y)

print(ans)
