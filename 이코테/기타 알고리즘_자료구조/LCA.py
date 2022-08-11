# LCA(최소 공통 조상) 알고리즘
# N(노드 개수) : 최대 50,000 개 / M(두 노드의 쌍) : 최대 10,000 개 -> O(NM) 가능
import sys

sys.setrecursionlimit(int(1e5))  # 런타임 오류 피하기

n = int(input())

parent = [0] * (n + 1)  # 부모 노드 정보
d = [0] * (n + 1)  # 각 노드까지의 깊이
c = [0] * (n + 1)  # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)]  # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
# 매 노드마다 깊이 값을 기록하고 -> 그 노드와 인접한 다른 노드를 확인하며
# -> 인접한 노드에 대해 깊이를 구했다면 넘기고, 그렇지 않으면 (현재까지 노드의 깊이 + 1) 을 통해 깊이를 대입하도록 함
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:  # 이미 깊이를 구한경우 -> 넘기기
        if c[y]:
            continue
        parent[y] = x
        dfs(y, depth + 1)


# A와 B의 최소 공통 조상을 찾는 함수
# 1) 먼저 A와 B의 깊이가 서로 다르다면, 깊이가 더 깊은 곳이 부모 쪽으로 이동하도록 만들어 -> 깊이가 같아지도록 하고
# 2) 이제, 노드가 같아질 때까지 부모 방향으로 동시에 이동하도록 만들기
def lca(a, b):
    # 먼저 깊이(depth)가 동일하도록
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 두 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


dfs(1, 0)  # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
