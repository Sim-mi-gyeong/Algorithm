# 그림
# 런타임 에러(1 1 / 0) -> 예외 처리 !!
from collections import deque

n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

lst = []   # 그림 종류를 담을 list