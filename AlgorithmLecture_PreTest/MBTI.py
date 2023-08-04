cost = {
    "ENFJ": 0,
    "ENFP": 0,
    "ENTJ": 0,
    "ENTP": 0,
    "ESFJ": 0,
    "ESFP": 0,
    "ESTJ": 0,
    "ESTP": 0,
    "INFJ": 0,
    "INFP": 0,
    "INTJ": 0,
    "INTP": 0,
    "ISFJ": 0,
    "ISFP": 0,
    "ISTJ": 0,
    "ISTP": 0,
}


mbti = [0] * 16
cnt = dict()
i = 0
for key in cost.keys():
    mbti[i] = key
    i += 1

alpha = {"E": 0, "S": 0, "T": 0, "J": 0, "I": 0, "N": 0, "F": 0, "P": 0}


tmp = 0
result = set()


def dfs(depth, num):
    global tmp
    if depth == 16:
        for i in result:
            tmp += cost[i]
        return

    dfs(depth + 1, num + lst[depth])  # 선택하는 경우
    dfs(depth + 1, num)  # 선택하지 않는 경우

    pass


def solution(dic, n):
    ans = 0
    minVal = 1e9
    visited = [0] * 16

    return ans


t = int(input())
for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    i = 0
    for key, val in cost.items():
        cost[key] = lst[i]
        cnt[key] = 0
        i += 1
    print("dic : ", cost)  # 비용

    solution(cost, n)
