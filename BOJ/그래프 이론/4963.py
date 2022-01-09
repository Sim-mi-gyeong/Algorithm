# 섬의 개수
import sys
sys.setrecursionlimit(100000)
def dfs(x, y):
    if x < 0 or y < 0 or x >= b or y >= a:
        return False

    if case[x][y] == 1:
      case[x][y] = 0
    
      dfs(x-1, y)
      dfs(x+1, y)
      dfs(x, y-1)
      dfs(x, y+1)
      dfs(x-1, y-1)
      dfs(x-1, y+1)
      dfs(x+1, y+1)
      dfs(x+1, y-1)
      return True

    return False
    
while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  case = [list(map(int, input().split())) for _ in range(b)]
  cnt = 0

  for i in range(b):
    for j in range(a):
      if dfs(i, j) == True:
        cnt += 1
  print(cnt)