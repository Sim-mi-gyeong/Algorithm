# 2차원 배열의 합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
sumList = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 원래 값 + 위 + 왼쪽 - 대각선(위와 왼쪽 계산 시 이미 한 번씩 처리) 중복 제거용
        sumList[i][j] = lst[i-1][j-1] + sumList[i-1][j] + sumList[i][j-1] - sumList[i-1][j-1]

print(sumList)                   
for _ in range(k):
    i, j, x, y = map(int, input().split())   # 1 부터 시작
    # sumList[x][j-1] 와 sumList[i-1][y] 에서 겹치는 부분 sumList[i-1][j-1] 빼주기
    ans = sumList[x][y] - sumList[x][j-1] - sumList[i-1][y] + sumList[i-1][j-1]
    print(ans)