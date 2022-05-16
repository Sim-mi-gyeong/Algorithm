# 감시 피하기

n = int(input())
graph = [list(input().split()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
k = 3
teacherList = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "T":
            teacherList.append((i, j))


def check():
    # 모든 선생님마다
    for teacher in teacherList:
        # x, y = teacher
        for d in range(len(dx)):
            # 상 하 좌 우에 대해 실행할 때마다 처음 위치 초기화 !!
            x, y = teacher
            # 상 하 좌 우에 대해 -> 각 방향마다 각 라인의 끝까지
            while 0 <= x < n and 0 <= y < n:
                if graph[x][y] == "O":
                    break
                elif graph[x][y] == "S":
                    # 한 선생님의 감시만 검사하는 것이 아닌, 모든 선생님들의 감시를 피해야 함
                    # 어떤 한 선생님의 감시에 걸린 경우
                    return False
                # "S"가 아니더라도, 즉 "X"가 나오면 다음 칸으로 이동해야 하므로
                x += dx[d]
                y += dy[d]

    # 모든 선생님들의 감시를 피한 경우
    return True


ans = "NO"


def dfs(cnt):
    global ans
    if cnt > k:
        return

    if cnt == k:
        if check():
            ans = "YES"
            return  # 현재 함수에서 빠져 나가 -> 그 함수를 호출했던 곳으로 되돌아 가라(한 가지 경우에 대해서라도 YES 를 만족하면)
        else:
            ans = "NO"

    for i in range(n):
        for j in range(n):
            if graph[i][j] == "X":
                graph[i][j] = "O"
                dfs(cnt + 1)
                # 추가
                if ans == "YES":
                    return
                # 백트래킹을 위한 초기화
                graph[i][j] = "X"


dfs(0)
print(ans)

"""
4
X S X T
X X S X
X X X X
T T T X

ans : YES

# 이 반례에서 걸림
5
X X S X X
X X X X X
S X T X S
X X X X X
X X S X X

ans : NO

5
X T X T X
T X S X T
X S S S X
T X S X X
X T X X X

ans : YES

5
X T X T X
T X S X T
X S S S X
T X S X X
X T X X X

ans : YES

5
X S S S X
T X X S X
X T X S X
X X T X S
X X X T X

ans : Yes
"""

