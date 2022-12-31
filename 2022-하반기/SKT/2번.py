import sys

input = sys.stdin.readline

n = int(input())
incomes = []
kills = []

for _ in range(n):
    incomes.append(list(map(int, input().split())))
    kills.append(list(map(int, input().split())))


alives = [0 for _ in range(n)]

# 누적을 최대로 많이 할 수 있는 경우가 여러가지 라면,
# 그럴 때엔, 수열을 고르는 순서가 사전순으로 앞서는 경우(첫번째 원소)를 출력
maxSaved, maxPath = -1, []  # 정답을 기록할 얼마를 누적했을 때 제일 많은 값인자, 그때의 내가 어떤 순서로 담았는지 기록할 배열


def backtracking(day, alives, saved, path):
    """
    [재귀함수는 함수의 역할을 잘 정의! 하는 것이 필요]
    0 ~ day - 1 일까지 잘 골라왔고,
    그때 지금 순간 배열은 alives 상태이고,
    현재까지 saved 만큼 누적되었으며,
    선택한 원소들은 path 에 저장되어 있는 상태이다.

    day ~ 4 일 (0일 ~ 4일) 까지 남은 모든 시나리오를 전부 탐색해주는 함수이다.
    """
    global maxSaved, maxPath

    # day = 5 인 경우, 0일부터 ~ 4일까지 잘 선택한 경우
    # 지금까지 고른 경우가 최대 누적값보다 큰 경우, 갱신 후 리턴
    if day == 5:
        if saved > maxSaved:
            maxSaved = saved
            maxPath = path

        return

    # 그게 아니라면, 현재 day 일(day 번째 라운드) 에 대해 + a / - a 를 진행
    # 그 값이 음수라면, 0으로 바꾸어 주어 배열의 상태 변경
    for i in range(n):
        alives[i] += incomes[i][day]
        alives[i] -= kills[i][day]
        if alives[i] < 0:
            alives[i] = 0

    # 이번 라운드에서 어떤 값을 누적시킬지 결정하고

    for i in range(n):
        val = alives[i]  # i 번째를 선택한다고 하면, 그 위치의 값을 저장하고
        alives[i] = 0  # 그 위치의 값을 0으로 바꾸고
        # 다음 날짜부터 가능한 모든 시나리오를 수행
        # 다음 날짜부터 시작해서, 현재 상태를 넘겨주고, 이때까지 누적한 값에 + 이번에 선택한 값 누적, 이번에 선택한 값을 path 에 추가
        # alives[:] : deepCopy (-> Call By Value, Call By Reference 를 피하기 위해) 를 위해 사용
        backtracking(day + 1, alives[:], saved + val, path + [i + 1])
        alives[i] = val


# 모든 가능한 시나리오를 모두 확인하고 -> 그때동안 제일 많이 누적했을 때를 찾기
backtracking(0, alives, 0, [])
print(maxSaved)
print(*maxPath)

"""
2
10 10 10 10 10
7 10 5 10 5
5 5 13 5 10
0 5 0 35 5
=>
31
1 1 2 1 1
"""

