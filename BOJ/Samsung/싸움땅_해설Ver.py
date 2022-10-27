import heapq


n, m, k = map(int, input().split())
# 2차원 그래프의 각 격자를 리스트로 초기화 및 입력받기!!
gun = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        # 총이 놓여있는 경우
        if tmp[j] != 0:
            # 이때, 각 격자는 우선순위 큐 방식으로 append ! -> 내림차순
            heapq.heappush(gun[i][j], -tmp[j])
            # gun[i][j].append(tmp[j])
print(gun)
# 플레이어 정보 입력받기
player = [(-1, -1, -1, -1, -1, -1)]  # 인덱스 = 플레이어 번호 를 위한 인덱스 0번 처리
for i in range(1, m + 1):
    x, y, d, s = map(int, input().split())
    player.append(
        [i, x - 1, y - 1, d, s, 0, 0]
    )  # 각 플레이어 자신의 번호, x 좌표, y 좌표, 방향, 초기 능력치, 보유한 총의 공격력, 획득한 포인트

print(player)
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 각 플레이어 포인트 정보 기록
point = [0] * (m + 1)  # 중요한 정보는 따로 리스트 등에 저장하는 것도 !

# class Player:
#     def __init__(self, num = 0, x=-1, y=-1, d=-1, power = 0, gun = 0):
#         self.num = num
#         self.x = x
#         self.y = y
#         self.d = d
#         self.power = power
#         self.gun = gun


def check_loc(nx, ny):
    if not (0 <= nx < n and 0 <= ny < n):
        return False


# player_num 번 사람이 현재 부딪힌 사람을 찾아주는 함수
# - 다른 사람의 위치를 보면서, 내 위치와 같은 경우 싸워야 하는 상황
# def conflict(player_num):
#     for other_player_num in range(1, m + 1):
#         if player_num == other_player_num:
#             continue
#         # 자신의 (x, y) 좌표가 다른 사람의 (x, y) 좌표와 같은 경우
#         if (player[player_num][1] == player[other_player_num][1]) and (
#             player[player_num][2] == player[other_player_num][2]
#         ):
#             return other_player_num

#     # 아무도 부딪히지 않는 경우 -> 0 을 리턴
#     return 0


# i 번 사람이 규칙에 맞게 이동하는 함수
def move(player_num):
    x, y, dir = player[player_num][1], player[player_num][2], player[player_num][3]
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not check_loc(nx, ny):
        dir ^= 2
        nx = x + dx[dir]
        ny = y + dy[dir]

    player[player_num][1] = nx
    player[player_num][2] = ny


# i 번 사람이 현재 위치에서 총을 줍는 함수
def pick_gun(player_num):
    x, y = player[player_num][1], player[player_num][2]
    print("(x, y) : ", (x, y))
    if len(gun[x][y]) == 0:
        return
    else:
        max_power_gun = -heapq.heappop(gun[x][y])
        player[player_num][5] = max_power_gun
        print("max_power_gun : ", max_power_gun)


def drop_gun(player_num):
    x, y = player[player_num][1], player[player_num][2]
    player_gun = player[player_num][5]
    heapq.heappush(gun[x][y], -player_gun)
    player[player_num][5] = 0


# x, y 에 존재하는 플레이어 번호를 찾는 함수 : 위의 coflict 함수 수정
def conflict(player_num, x, y):
    for other_player_num in range(1, m + 1):
        if player_num == other_player_num:
            continue
        # 자신의 (x, y) 좌표가 다른 사람의 (x, y) 좌표와 같은 경우
        elif (x == player[other_player_num][1]) and (y == player[other_player_num][2]):
            return other_player_num

    return 0


# 승자와 패자에 대한 각 처리가 다르므로 -> 모듈화
# 승자에 대한 처리 함수
def winner(player_num):
    # 자기가 가진 총을 먼저 땅에 놓고
    drop_gun(player_num)
    # 그런 다음 줍기
    # -> 이렇게 하면, 내가 가진 총을 포함해서 가장 공격력이 높은 총을 주울 수 있음
    pick_gun(player_num)


# 패자에 대한 처리 함수
def loser(player_num):
    # 1. 총을 먼저 내려 놓고
    drop_gun(player_num)
    # 2. 자신이 가려고 했던 방향으로 이동
    x, y, dir = player[player_num][1], player[player_num][2], player[player_num][3]
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 3. 만약, 이동하려고 하는 위치가 1) 격자를 벗어나거나 2) 다른 사람이 있으면 -> 90도 회전해서 이동
    while not check_loc(nx, ny) or conflict(player_num, nx, ny):
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]

    # Player 의 위치/방향 정보 업데이트
    player[player_num][1], player[player_num][2], player[player_num][3] = nx, ny, dir

    # 4. 총이 있는 경우 총 줍기
    pick_gun(player_num)


# i 번 사람과 j 번 사람이 싸우는 함수
def fight(i, j):
    # 1. 두 사람의 점수 비교
    print(i, " 번 사람과 ", j, " 번 사람이 fight")
    score_i = player[i][4] + player[i][5]
    score_j = player[j][4] + player[j][5]

    if score_i == score_j:
        # 초기 능력치로 비교
        if player[i][4] < player[j][4]:
            print(j, " 번 사람이 이긴 경우")
            # j 번 사람 승리
            # 승리자에 대한 점수 업데이트 먼저
            player[j][6] += abs(score_i - score_j)
            point[j] += abs(score_i - score_j)
            winner(j)
            loser(i)
        else:
            print(i, " 번 사람이 이긴 경우")
            # i 번 사람 승리
            player[i][6] += abs(score_i - score_j)
            point[i] += abs(score_i - score_j)
            winner(i)
            loser(j)
    # j 번 승리 (즉, 나 말고 다른 사람이 이기는 경우)
    elif score_i < score_j:
        print(j, " 번 사람이 이긴 경우")
        player[j][6] += abs(score_i - score_j)
        point[j] += abs(score_i - score_j)
        winner(j)
        loser(i)
    # i 번 승리 (즉, 나 말고 다른 사람이 이기는 경우)
    else:
        print(i, " 번 사람이 이긴 경우")
        player[i][6] += abs(score_i - score_j)
        point[i] += abs(score_i - score_j)
        winner(i)
        loser(j)


def pro():
    # global k
    for _ in range(k):
        # 모든 사람들에 대해 이동시키기
        for player_num in range(1, m + 1):
            print("player_num : ", player_num)
            move(player_num)
            fight_player_num = conflict(player_num, player[player_num][1], player[player_num][2])
            print("fight_player_num : ", fight_player_num)
            # 싸움이 일어나지 않는다면
            if fight_player_num == 0:
                drop_gun(player_num)
                pick_gun(player_num)  # 총을 줍고
            else:
                fight(player_num, fight_player_num)

    # 각 사람들이 가진 점수 출력
    for i in range(1, m + 1):
        print(point[i], end=" ")
    print()
    for i in range(1, m + 1):
        print(player[i][6], end=" ")


def solve():
    pro()


solve()


"""
5 4 2
1 2 0 1 2
1 0 3 3 1
1 3 0 2 3
2 1 2 4 5
0 1 3 2 0
1 3 2 3
2 2 1 5
3 3 2 2
5 1 3 4

3 5 1
0 5 0
0 0 4
5 3 0
1 1 0 2
3 3 2 1
1 3 2 5
2 1 1 3
2 2 1 4

"""

