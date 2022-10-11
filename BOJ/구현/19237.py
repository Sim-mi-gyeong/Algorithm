# 어른 상어

# 상어는 1 ~ M 번호 - 모든 번호 서로 다름
# 영역 사수를 위해 다른 상어를 쫓아냄
# 번호 1 은 가장 강력해서 나머지 쫓아낼 수 있음

# N * N 공간 중 M 개의 칸에 상어 한 마리씩

# 1. 모든 상어가 자신의 냄새를 뿌림
# 2. 이후 1초마다 모든 상어가 동시에 상하좌우 인접 칸 중 하나로 이동 -> 자신의 냄새를 뿌림
# 2-1. 냄새는 상어가 k 번 이동하고 나면 사라진다.
# 2-2. 각 상어 이동 방향 결정 : 인접칸 중 아무 냄새가 없는 칸의 방향으로
# -> 그런 칸이 없으면, 자신의 냄새가 있는 칸의 방향으로 잡음
# -> 이때도 여러 칸이면, 특정한 우선순위를 따름 (상어 종류마다, 현재 상어의 시야 방향에 따라 다름)
# -> 상어의 처음 시야 방향은 입력으로 주어지고 -> 이후 방금 이동한 방향이 보고있는 방향 = 시야 방향

# 3. 모든 상어 이동 후 한 칸에 여러 마리의 상어가 남아 있으면 -> 가장 작은 번호 상어만 남고 쫓겨남

# 왼쪽 하단 정수 = 냄새 -> 값 : 사라지기까지 남은 시간
# 왼쪽 상단 정수 = 상어의 번호 or 냄새를 뿌린 상어의 번호

# 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하기
import sys

input = sys.stdin.readline
# 방향(상 하 좌 우)
# 1 - 위 / 2 - 아래 / 3 - 왼쪽 / 4 - 오른쪽
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())
graph = []
# 0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸
shark = []  # 남아있는 상어 확인용 리스트
# shark_loc_dic = []  # 상어의 초기 위치 저장 -> 이후 변경된 위치도 전역적으로 적용
shark_loc_dic = dict()
info_graph = [[[0] * 2 for _ in range(n)] for _ in range(n)]
# 처음 위치에서 향수 뿌리기
def init_smell(sharkX, sharkY, sharkNum):
    global info_graph
    info_graph[sharkX][sharkY][0] = sharkNum
    info_graph[sharkX][sharkY][1] = k


for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(n):
        if tmp[j] != 0:
            graph[i][j] = tmp[j]
            shark.append(tmp[j])
            init_smell(i, j, tmp[j])
            shark_loc_dic[tmp[j]] = (i, j)

print("상어의 초기 위치 : ", shark_loc_dic)
print("처음 향수가 뿌려진 상태 : ", info_graph)

### 각 상어의 현재 방향 입력 받기
dir_input = list(map(int, input().split()))
shark_dir_dic = dict()
for i in range(1, m + 1):
    shark_dir_dic[i] = dir_input[i - 1]

# 각 상어의 방향 우선순위 - m 마리 중 각 상어마다 4줄씩 - 상 좌 하 우 를 향할 때 순서로 우선순위
sharkDir = []
for _ in range(m):
    # 각 상어의 전체 방향 우선순위
    totalDir = []
    for i in range(4):
        # 각 상어의 방향 별(상 - 하 - 좌 - 우) 우선순위
        tmp = list(map(int, input().split()))
        totalDir.append(tmp)
    sharkDir.append(totalDir)

# 상어가 이동하면서 향수를 뿌리는 정보를 기록할 그래프 - 3차원
# -> 해당 그래프에서 각 격자는 (향수를 뿌린 상어 번호, 향수 남은 시간(k))
# graph : 상어의 이동에 따른 그래프
# info_graph = [[[0] * 2 for _ in range(n)] for _ in range(n)]


# 맨 처음에는 상어마다 인접한 빈 칸 존재 -> 처음부터 이동을 못 하는 경우는 없음
# 상어 이동 과정에서 한 칸에 여러 마리 -> 가장 작은 번호 상어가 남기때문에 번호가 작은 상어부터 이동 처리 (X)
### 모든 상어가 동시에 이동해야해!!!!!
def move_shark_and_smell():
    global shark_dir_dic, shark_loc_dic, shark, k, graph, info_graph
    # 각 상어의 이동 후 위치 저장 - 상어가 쫓겨날 수 있기 때문에 빈 상어 번호가 생길 수 있어, 인덱스 발고 key 로 구분을 위해 dic
    # move_shark_loc_dic = dict()
    # 작은 번호 순으로, 각 상어마다
    for i in range(1, m + 1):
        print(i, "번 상어 이동 시작!\n")

        # for sharkIndex in range(len(shark)):
        #     i = shark.index(shark)
        check = False
        # 상어가 존재하지 않는 경우
        if i not in shark:
            continue
            # break   # break 를 해버리니까, shark : [3, 1] 인 상태에서, 2번 상어 이동 시작! 을 외치고 -> 2번 상어가 없으니까 바로 종료하는 것!! -> continue 처리

        # 상어의 현재 위치 : shark_loc_dic 딕셔너리로 부터, 상어 번호를 통해 찾기
        currX, currY = shark_loc_dic[i][0], shark_loc_dic[i][1]
        print(i, " 번 상어의 현재 위치 (currX, currY) : ", (currX, currY))
        # 상어의 현재 방향
        currDir = shark_dir_dic[i]  # 1번 상어 - 4 / 2번 상어 - 4 / 3번 상어 - 3 / 4번 상어 - 1 상태
        # 현재 방향 기준 - 방향 우선 순위를 통해 -> 다음 이동 방향 찾기
        for j in range(1, 4 + 1):
            # for j in range(4):
            print(i, " 번 상어의 현재 방향 기준 우선순위 : ", sharkDir[i - 1][currDir - 1])  # 4 3 1 2
            nextDir = sharkDir[i - 1][currDir - 1][j - 1]
            # dx[] 의 인덱스로 들어갈 값이어야 함
            nx = currX + dx[nextDir]  # dx, dy 의 인덱스 0번째 -> 0 으로 처리
            ny = currY + dy[nextDir]
            # print(i, " 번 상어의 (nx, ny) : ", (nx, ny))
            # 다음 위치로 이동 가능한지 확인 - 냄새가 없는 위치로
            # 범위 넘어가지 않는지 체크
            if 0 <= nx < n and 0 <= ny < n:
                # 이동하고자 하는 위치에, 상어는 존재하지 않고 향기도 존재하지 않는 경우 (향기가 뿌려지고 난 이후) -> 이동 가능
                # if info_graph[nx][ny][0] == 0 and graph[nx][ny] == 0:
                if info_graph[nx][ny][0] == 0:
                    print(i, " 번 상어가 이동할 위치 : ", (nx, ny))
                    # 이동 후 상어의 위치 기록
                    graph[nx][ny] = i
                    # 이동 전 상어의 위치는 빈칸 처리
                    graph[currX][currY] = 0
                    shark_loc_dic[i] = (nx, ny)
                    # 이동 후 상어의 이동 방향 기록
                    shark_dir_dic[i] = nextDir
                    print(i, " 번 상어의 다음 방향 : ", nextDir)
                    # 이동 후 냄새 뿌리기
                    info_graph[nx][ny][0] = i  # 자신의 번호
                    info_graph[nx][ny][1] = k  # 남은 시간 세팅
                    check = True  # 자신의 처리 완료
                    break
                # 이동하고자 하는 위치에, 이전 번호인 상어가 금방 들어와서 향수를 뿌린 경우, 상어가 아직 존재하는 경우 -> 이동 가능
                # 동시에 이동하기 때문에, 빈 공간일 줄 알고 갔는데 자기보다 번호가 작은 상어가 존재하는 경우
                elif info_graph[nx][ny][1] == k and graph[nx][ny] != 0:
                    # 잡아 먹힘
                    print(i, " 번 상어가 잡하먹힐 수 있는 위치 : ", (nx, ny))
                    print("몇 번 상어가 잡아먹혀야 할 지 : ", i)
                    print("잡아먹힐 때 그래프 상태 : ", graph, "\n")
                    print("잡아먹힐 때 향수 정보 상태 : ", info_graph, "\n")
                    graph[currX][currY] = 0  # 이전 위치는 빈 칸으로 하고
                    shark.remove(i)
                    check = True  # 자신의 처리 완료
                    break

        if check:
            continue
        # 네 방향을 다 돌았는데에도 향수를 뿌릴 수 있는 위치가 없는 경우 -> 자신의 냄새가 있는 칸으로 방향 잡기
        # 이때, 칸이 여러개면? -> 우선순위에 따라
        # 현재 위치 기준 자신의 냄새가 있는 쪽 찾기
        print("자신이 뿌린 향수가 있는 위치로 와야 하는 상어 : ", i, " 번 상어")

        ### 현재 위에서 자리 잡은 경우에도, 여기로 넘어는 것임
        ### 위에서 for j in range(1, 4 + 1): 이 반복문만 빠져나가는 상태

        tmp_next_move_list = []
        for j in range(1, 4 + 1):
            nx2 = currX + dx[j]
            ny2 = currY + dy[j]
            if 0 <= nx2 < n and 0 <= ny2 < n:
                # 향수가 뿌려진 위치가 자신이 뿌린 향수라면
                if info_graph[nx2][ny2][0] == i:
                    # 그 위치로 이동할 경우에, 방향도 같이 기록하기
                    # (nx2, ny2) 로 가려면 k 방향으로 틀어야 한다는 것
                    tmp_next_move_list.append((nx2, ny2, k))

        # 대안으로 이동가능한 위치들 중, 우선순위에 따라
        curr_priority_dir_list = sharkDir[i - 1][currDir - 1]
        for priority_dir in curr_priority_dir_list:
            for tmp_next_move in tmp_next_move_list:
                tmp_next_x = tmp_next_move[0]
                tmp_next_y = tmp_next_move[1]
                tmp_next_dir = tmp_next_move[2]
                if priority_dir == tmp_next_dir:
                    # 다음 위치는 tmp_next_dir 방향으로 결정
                    # tmp_next_x, tmp_next_y 가 다음 위치
                    # 이동 후 상어의 위치 기록
                    shark_loc_dic[i] = (tmp_next_x, tmp_next_y)
                    # 이동 후 상어의 이동 방향 기록
                    shark_dir_dic[i] = tmp_next_dir
                    # 이렇게 이동해서 온 위치에는, 이미 냄새가 있는 상태여서 뿌릴 수 없음
                    graph[tmp_next_x][tmp_next_y] = i
                    graph[currX][currY] = 0
                    print(i, " 번 상어가 자신이 뿌린 향수의 위치로 왔을 때 위치 : ", (tmp_next_x, tmp_next_y))


# 1. 모든 상어가 자신의 냄새를 뿌림
# 2. 이후 1초마다 모든 상어가 동시에 상하좌우 인접 칸 중 하나로 이동 -> 자신의 냄새를 뿌림
# 2-1. 냄새는 상어가 k 번 이동하고 나면 사라진다.
# 2-2. 각 상어 이동 방향 결정 : 인접칸 중 아무 냄새가 없는 칸의 방향으로
# -> 그런 칸이 없으면, 자신의 냄새가 있는 칸의 방향으로 잡음
# -> 이때도 여러 칸이면, 특정한 우선순위를 따름 (상어 종류마다, 현재 상어의 시야 방향에 따라 다름)
# -> 상어의 처음 시야 방향은 입력으로 주어지고 -> 이후 방금 이동한 방향이 보고있는 방향 = 시야 방향

# 3. 모든 상어 이동 후 한 칸에 여러 마리의 상어가 남아 있으면 -> 가장 작은 번호 상어만 남고 쫓겨남

# sharkDir
# [
#  [[2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 2, 1], [4, 3, 1, 2]],
#  [[2, 4, 3, 1], [2, 1, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]],
#  [[4, 3, 2, 1], [1, 4, 3, 2], [1, 3, 2, 4], [3, 2, 1, 4]],
#  [[3, 4, 1, 2], [3, 2, 4, 1], [1, 4, 2, 3], [1, 4, 2, 3]]
# ]

# 각 초마다 향수가 존재하는 위치의 향수 남은 시간 - 1
# info_graph 각 위치는 (냄새 뿌린 상어 번호, 시간)
def schedule():
    global info_graph
    for i in range(n):
        for j in range(n):
            # 1초만 남아있는 경우 -> 그 위치 흔적 제거(초기화 상태로)
            if info_graph[i][j][1] == 1:
                info_graph[i][j][0] = 0
                info_graph[i][j][1] = 0
            # 1초 보다 더 많이 냄새가 아직 남아 있으면
            elif info_graph[i][j][1] >= 1:
                # 1 초씩 줄이기
                info_graph[i][j][1] -= 1


# 1번 상어만 남았는지 확인하는 함수
def chek_shark_exist():
    if len(shark) == 1 and shark[0] == 1:
        return True
    return False


time = 0
check = True
# init_smell()
print(time, " 초 지남 ")
while True:

    if chek_shark_exist():
        break

    # if time >= 1000:
    if time >= 1000:
        check = False
        break

    move_shark_and_smell()
    # print("shark 상태 : ", shark)
    # print(time + 1, " 시간 일 때, graph 상태 : ", graph)
    # print()
    # print(time + 1, " 시간 일 때, info_graph 상태 : ", info_graph)
    schedule()

    time += 1
    print()
    print(time, " 초 지남")
    print()
    print("살아있는 상어 상태  :", shark)
    print("graph 상태 ")
    print(graph)
    print()

if check:
    print(time)
else:
    print(-1)
