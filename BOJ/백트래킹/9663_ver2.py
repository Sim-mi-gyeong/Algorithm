# N-Queen(1차원 베열)

import sys
input = sys.stdin.readline
n = int(input())
board = [0 for _ in range(n)]    # 인덱스 번호 = 행 / 인덱스 값 = 열
cnt = 0

def isAble(x):
    # 이미 놓여진 퀸과 같은 열이거나 / 대각선에 위치한다면,
    for i in range(x):   # 하나의 열에서, 각 행에 대해
        if board[x] == board[i] or abs(x - i) == abs(board[x] - board[i]):
            return False
    return True

# 여기서 인자값인 x는 행의 위치
def nQeeen(x):
    global cnt
    if x == n: cnt += 1   # n개를 모두 놓았을 때 -> 1가지 방법 추가
    else:
        for i in range(n):   # 각 열에 대해 -> 처음 시작은 0행의 각 열에 대해
            # 일단 한 군데에 놓고
            board[x] = i   # 차음 시작은 0행의 0(i)열에 놓고
            if isAble(x):   # 퀸 놓기 조건에 맞다면
                nQeeen(x+1)   # 다음 행으로
            
nQeeen(0)
print(cnt)