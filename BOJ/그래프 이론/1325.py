# 효율적인 해킹

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
rel = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    rel[b].append(a)   # 해킹의 주체는 b (b의 인덱스에 해킹 가능한 번호추가)
queue = deque([])

def bfs(start, rel, visited):
    queue.append(start)
    visited[start] = 1
    cnt = 1
    while queue:
        v = queue.popleft()
        for i in rel[v]:
            if visited[i] == 0:   # 방문하지 않았으면, 
                visited[i] = 1
                queue.append(i)
                cnt += 1
    return cnt   # return 값으로 특정한 값(해킹하는 컴퓨터의 수)을 반환할 때 -> visted[i] + 1 대신 cnt += 1

result = []
maxCnt= 0
for i in range(1, n+1):   # 시작 시점이 정해지지 않음
    visited = [0] * (n+1)
    ans = bfs(i, rel, visited)
    if maxCnt < ans:
        maxCnt = ans
    result.append((i, ans))   # (index, cnt) 로 두 가지 정보 저장 가능 -> 따로, 최댓값일 때만 result로 업데이트 하지 않아도 됨

for i, ans in result:
    if ans == maxCnt:
        print(i, end = ' ')