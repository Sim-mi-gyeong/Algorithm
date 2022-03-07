# N-Queen(1차원 배열)
# 1) 상하좌우 같은 줄에 이미 위치한 퀸(Queen)이 있는가?
# 2) 대각선의 같은 줄에 이미 위치한 퀸(Queen)이 있는가?
# -> 1), 2) 해당 : 다음 퀸을 놓지 않고 이전 상태로 돌아가 다시 퀸을 놓는다(백트래킹)
# -> 1), 2) 해당 X : 다음 퀸을 놓는다.
# 현재 놓는 퀸이 N번째(마지막) 퀸(Queen)인가?
# -? O : 정답 -> 퀸을 놓는 경우의 수 += 1
# =? X : 다음 퀸을 놓는다. 

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0   # 경우의 수
row = [0] * n

def isAble(x):
    # 이미 놓여진 퀸과 같은 열이거나/대각선 상에 있는지 확인
    # x/i : 행, row[x]/row[i] : 열
    # if (행끼리의 차 == 열 끼리의 차의 절댓값) => True(대각선상)
    for i in range(x):
        if (row[x] == row[i]) or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def nQueens(x):
    global cnt
    if x == n: cnt += 1
    else:
        for i in range(n):
            # row[i] = j : (i, j)에 퀸을 놓는다
            row[x] = i
            if isAble(x):
                nQueens(x+1)
nQueens(0)
print(cnt)