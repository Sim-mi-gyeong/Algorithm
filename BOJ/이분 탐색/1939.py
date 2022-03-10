# 중량제한 - BFS & 이진탐색
# 최소와 최대 중량 지정 -> mid를 통해 중간값을 계산해, BFS를 통해 목적지 도달 가능 여부 판단
# 트럭이 존재한다고 할 때, 중량 조절을 통해 트럭이 다리를 통과할 수 있는지 판단

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
distance = [0] * (n+1)   # 최대인 중량을 구하므로 0으로 초기화
for _ in range(m):
    a, b, cost = map(int, input().split())
    lst[a].append((cost, b))
    lst[b].append((cost, a))

for i in range(n+1):
    lst[i].sort(reverse=True)

x, y = map(int, input().split())
# 중량 범위 : 1 ≤ C ≤ 1,000,000,000
start, end = 1, 1000000000

def bfs(mid):
    visited[x] = 1   # 처음 시작 위치 방문 처리
    queue = deque()
    queue.append(x)

    while queue:
        v = queue.popleft()
        if v == y:
            return True   # 도달 가능한 상태
        for weight, next in lst[v]:
            if visited[next] == 0 and mid <= weight:   # 기준 중량보다는, 다리의 무게가 더 큰 값이어야 함
                queue.append(next)
                visited[next] = 1

    return False

while start <= end:
    visited = [0] * (n+1)
    mid = (start + end) // 2
    if bfs(mid):   # 목적지까지 도달 가능 -> 오른쪽 탐색
        result = mid
        start = mid + 1
    else:   # 목적지까지 도달 불가능 -> 왼쪽 탐색
        end = mid - 1 

print(result)
# result = mid 대신 end 값을 출력할 수 있는 이유는, 
# 이전까지 bfs를 반복 실행해서 True 였다가, start = mid + 1 로 변경한 후 bfs를 수행했을 때에는 도달 불가능한, 즉 멈춰야 하는 경우이며, 
# 이때 return Flase를 받아 else: end = mid - 1이 실행되기 때문 
print(end)   

'''
[입력 예시]
6 9
1 2 7
1 3 8
1 4 7
1 6 9
2 3 7
3 4 7
3 5 7
4 5 7
4 6 7
6 3
[출력 예시]
8

[입력 예시]
3 3
1 2 2
3 1 3
2 3 2
1 3
[출력 예시]
3
'''