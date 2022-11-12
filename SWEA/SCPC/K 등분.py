def prefixSum(n, k, lst):
    prefixSumList = [0 for _ in range(n)]
    prefixSumList[0] = 0
    for i in range(1, n):
        prefixSumList[i] = prefixSumList[i - 1] + lst[i]

    return prefixSumList


def solution(n, k, lst):
    prefix = prefixSum(n, k, lst)
    dp = [[0] * k for _ in range(n)]
    ans = 0
    # 전체 합이 k 로 나누어 떨어져야 함
    partVal = sum(lst) // k
    if partVal % k != 0:
        return 0
    dp[0][0] = 1

    for i in range(1, n):
        print("i : ", i)
        dp[i][0] = 1
        for j in range(1, k):
            # print("i, j : ", i, j)
            dp[i][j] = dp[i - 1][j]
            # print(dp)
            # print()
            print("partVal * j : ", partVal * j, " prefix[i] : ", prefix[i])
            if partVal * j == prefix[i]:
                dp[i][j] += dp[i - 1][j - 1]
    print("dp")
    print(dp)
    return dp[n - 1][k - 1]


# dp[i][j] 정의 : i 번째까지 j번으로 나누는 경우의 수
t = int(input())

for tc in range(t):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = solution(n, k, lst)
    print("Case #{}".format(tc + 1))
    print(ans)


"""
3
8 6
3 2 -2 3 3 3 3 3
6 2
1 0 2 -1 3 -3
10 6
1 1 -1 1 1 1 1 1 -1 1
"""

"""
1
8 6
3 2 -2 3 3 3 3 3
"""
