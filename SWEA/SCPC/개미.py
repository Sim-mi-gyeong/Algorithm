def solution(n, pos, val):
    initDic = {}
    for i in range(n):
        initDic[pos[i]] = val[i]

    sortValDic = dict(sorted(initDic.items(), key=lambda x: x[1]))

    initPos = [k for k in initDic.keys()]
    sortPos = [k for k in sortValDic.keys()]
    ans = 0
    for i in range(n):
        ans += abs(initPos[i] - sortPos[i])
    return ans


t = int(input())

for tc in range(t):
    n = int(input())  # 개미 수
    pos = list(map(int, input().split()))  # 개미 위치
    val = list(map(int, input().split()))  # 개미가 들고 있는 값
    ans = solution(n, pos, val)
    print("Case #{}".format(tc + 1))
    print(ans)


# 우선, val 을 정렬하고 -> 각 val 을 정렬했을 때 이동 가능한 경우에 대해 탐색


"""
3
5
1 2 4 5 6
9 2 1 1 2
5
1 2 7 8 10
7 3 3 3 7
5
4 5 6 7 10
9 10 10 10 9
"""

