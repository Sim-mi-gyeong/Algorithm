def exist_gun(nx, ny):
    exist = True
    if len(graph_gun[nx][ny]) == 0:
        exist = False
    return exist


def get_stronger_gun(player_num, nx, ny):
    global player, graph, graph_gun, graph_player
    if exist_gun(nx, ny):
        if player[player_num][4] == 0:
            max_power_gun = max(graph_gun[nx][ny])
            player[player_num][4] = max_power_gun
            graph_gun[nx][ny].remove(max_power_gun)

        else:
            my_gun_power = player[player_num][4]
            get_gun_list = graph_gun[nx][ny]
            max_get_gun_power = my_gun_power
            for tmp_gun in get_gun_list:
                if tmp_gun > my_gun_power:
                    max_get_gun_power = max(max_get_gun_power, tmp_gun)

            if max_get_gun_power > my_gun_power:
                player[player_num][4] = max_get_gun_power
                graph_gun[nx][ny].remove(max_get_gun_power)
                if my_gun_power != 0:
                    graph_gun[nx][ny].append(my_gun_power)
    else:
        pass


def fight(player_num, nx, ny):
    global player, graph, graph_gun, graph_player
    pre_player_num = graph_player[nx][ny]

    pre_player_total = player[pre_player_num][3] + player[pre_player_num][4]
    curr_player_total = player[player_num][3] + player[player_num][4]

    win_player_num, lose_player_num = 0, 0

    if pre_player_total == curr_player_total:
        if player[pre_player_num][3] > player[player_num][3]:
            win_player_num = pre_player_num
            lose_player_num = player_num
        else:
            win_player_num = player_num
            lose_player_num = pre_player_num

    elif pre_player_total > curr_player_total:
        win_player_num = pre_player_num
        lose_player_num = player_num

    else:
        win_player_num = player_num
        lose_player_num = pre_player_num

    point = abs(pre_player_total - curr_player_total)
    player[win_player_num][5] += point

    lose_player_gun = player[lose_player_num][4]
    if lose_player_gun != 0:
        graph_gun[nx][ny].append(lose_player_gun)
    player[lose_player_num][4] = 0

    my_gun_power = player[win_player_num][4]

    get_gun_list = graph_gun[nx][ny]
    max_get_gun_power = my_gun_power
    for tmp_gun in get_gun_list:
        if tmp_gun > my_gun_power:
            max_get_gun_power = max(max_get_gun_power, tmp_gun)

    if max_get_gun_power > my_gun_power:
        player[win_player_num][4] = max_get_gun_power
        graph_gun[nx][ny].remove(max_get_gun_power)
        if my_gun_power != 0:
            graph_gun[nx][ny].append(my_gun_power)

    lose_player_x, lose_player_y, lose_player_dir = (
        player[lose_player_num][0],
        player[lose_player_num][1],
        player[lose_player_num][2],
    )
    next_lose_player_x = lose_player_x + dx[lose_player_dir]
    next_lose_player_y = lose_player_y + dy[lose_player_dir]
    next_lose_player_dir = lose_player_dir

    if check_loc(next_lose_player_x, next_lose_player_y) and not exist_player(
        next_lose_player_x, next_lose_player_y
    ):
        pass

    else:
        ### 현재 방향 기준 오른쪽으로 90도 회전하면서 방향 바꾸다가 -> 빈칸(총 있는 곳도 OK) 보일 때까지
        for i in range(4):
            next_dir = (lose_player_dir + i) % 4
            next_lose_player_x = lose_player_x + dx[next_dir]
            next_lose_player_y = lose_player_y + dy[next_dir]
            if check_loc(next_lose_player_x, next_lose_player_y) and not exist_player(
                next_lose_player_x, next_lose_player_y
            ):
                next_lose_player_dir = next_dir
                break

    player[lose_player_num][0] = next_lose_player_x
    player[lose_player_num][1] = next_lose_player_y
    player[lose_player_num][2] = next_lose_player_dir

    ### 싸움 완료 후 위치
    graph_player[next_lose_player_x][next_lose_player_y] = lose_player_num
    graph_player[nx][ny] = win_player_num

    if exist_gun(next_lose_player_x, next_lose_player_y):

        my_gun_power = player[lose_player_num][4]
        get_gun_list = graph_gun[next_lose_player_x][next_lose_player_y]
        max_get_gun_power = my_gun_power
        for tmp_gun in get_gun_list:
            if tmp_gun > my_gun_power:
                max_get_gun_power = max(max_get_gun_power, tmp_gun)

        if max_get_gun_power > my_gun_power:
            player[lose_player_num][4] = max_get_gun_power
            graph_gun[next_lose_player_x][next_lose_player_y].remove(max_get_gun_power)
            if my_gun_power != 0:
                graph_gun[next_lose_player_x][next_lose_player_y].append(my_gun_power)


def exist_player(nx, ny):
    exist = False
    if graph_player[nx][ny] != 0:
        exist = True

    return exist


def check_loc(nx, ny):

    enable = False
    if 0 <= nx < n and 0 <= ny < n:
        enable = True
    return enable


def move(player_num):

    x, y, d, init_power, gun_power, point = (
        player[player_num][0],
        player[player_num][1],
        player[player_num][2],
        player[player_num][3],
        player[player_num][4],
        player[player_num][5],
    )
    nx = x + dx[d]
    ny = y + dy[d]
    if not check_loc(nx, ny):
        d ^= 2
        nx = x + dx[d]
        ny = y + dy[d]

    player[player_num] = [nx, ny, d, init_power, gun_power, point]

    if exist_player(nx, ny):
        graph_player[x][y] = 0
        fight(player_num, nx, ny)
    else:
        graph_player[x][y] = 0
        graph_player[nx][ny] = player_num
        get_stronger_gun(player_num, nx, ny)


def play():
    for player_num in range(1, m + 1):
        move(player_num)


def get_player_point():
    player_point_list = []
    for player_num in range(1, m + 1):
        one_player_point = player[player_num][5]
        player_point_list.append(one_player_point)
    return player_point_list


def solve():
    # k 라운드 동안 진행
    for tmpK in range(k):
        play()

    player_point_list = get_player_point()

    return player_point_list


n, m, k = map(int, input().split())
graph = []
graph_player = [[0] * n for _ in range(n)]
graph_gun = [[0] * n for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] > 0:
            graph_gun[i][j] = [tmp[j]]
        else:
            graph_gun[i][j] = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
player = [[-1, -1, -1, -1, -1, -1]]
for num in range(1, m + 1):

    x, y, d, s = map(int, input().split())
    player.append([x - 1, y - 1, d, s, 0, 0])
    graph_player[x - 1][y - 1] = num

ans = solve()
for point in ans:
    print(point, end=" ")
