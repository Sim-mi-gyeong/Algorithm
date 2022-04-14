# 부분 수열의 합 - combinations
# 투포인터 -> substring

from itertools import combinations

n, s = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(1, n + 1):
    comList = list(combinations(lst, i))
    for j in comList:
        if sum(j) == s:
            cnt += 1

print(cnt)

"""
5 0
-7 -3 -2 8 5

5 0
0 0 0 0 0
답 : 31
"""
