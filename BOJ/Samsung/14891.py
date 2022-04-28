# 톱니바퀴

from collections import deque

# rotate() : 리스트 회전 (양수: 오른쪽, 음수: 왼쪽 회전)
wheel = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())


def dfs(x, dir):
    # 회전시켜야 하는 target 톱니바퀴의 왼쪽 / 오른쪽 확인
    global visited
    if visited[x] == 0:
        visited[x] = 1
        left, right = wheel[x][6], wheel[x][2]
        if dir == 1:
            last = wheel[x].pop()
            wheel[x].appendleft(last)
        else:
            front = wheel[x].popleft()
            wheel[x].append(front)

        # target 의 회전은 회전대로 처리하고, 인접한 톱니바퀴들의 회전 여부/회전 방향은 재귀로 check
        # target 왼쪽 check
        if x - 1 >= 0 and left != wheel[x - 1][2]:
            dfs(x - 1, -dir)
        # target 오른쪽 check
        if x + 1 <= 3 and right != wheel[x + 1][6]:
            dfs(x + 1, -dir)


for _ in range(k):
    n, dir = map(int, input().split())
    visited = [0] * 4
    dfs(n - 1, dir)

total = 0
for i in range(4):
    if wheel[i][0] == 1:
        total += 2 ** i

print(total)
