from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n = int(input())
graph = []
teacher = []
student = 0
for i in range(n):
    tmp = list(input().split())
    graph.append(tmp)
    for j in range(n):
        if tmp[j] == "T":
            teacher.append((i, j))


def checkWatch():
    print("checkWatch 호출 시 graph : ", graph)
    q = deque(teacher)
    while q:
        x, y = q.popleft()
        # 상 하 좌 우 에 대해 실행할 때마다 -> 선생님이 위치한 시작 위치로!
        for i in range(len(dx)):
            teacherX, teacherY = x, y
            while 0 <= teacherX < n and 0 <= teacherY < n:
                if graph[teacherX][teacherY] == "O":
                    break
                elif graph[teacherX][teacherY] == "S":
                    return False
                teacherX += dx[i]
                teacherY += dy[i]

    return True


visited = [[0] * n for _ in range(n)]
ans = False


def install(cnt):
    global ans
    if cnt > 3:
        return
    if cnt == 3:
        check = checkWatch()
        if check:
            ans = True
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == "X":
                graph[i][j] = "O"
                install(cnt + 1)
                graph[i][j] = "X"


install(0)
if ans:
    print("YES")
else:
    print("NO")
