# LCA 2
# N(노드 개수) : 최대 100,000 개 / M(두 노드의 쌍) : 최대 100,000 개 -> O(NM) 시간 초과
# 각 노드가 거슬러 올라가는 속도 빠르게 해야 함
# 총 데이터가 최대 1,000,000 개 까지 들어올 수 있다고 가정

import sys

input = sys.stdin.readline  # 시간 초과를 피하기 위한 빠른 입력 함수
sys.setrecursionlimit(int(1e5))  # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정

# LOG 는, 최악의 경우(트리가 1렬로 늘어서는 경우)에 리프노드가 부모노드 정보를 모두 저장하기 위해서 필요한 값
# 2^20 = 1,000,000 -> 2^i 단위의 부모값을 저장하기 위한 크기 (1000000의 log2를 취한 값의 올림)
LOG = 21

n = int(input())
parent = [[0] * LOG for _ in range(n + 1)]  # 부모 노드 정보
d = [0] * (n + 1)  # 각 노드까지의 깊이
c = [0] * (n + 1)  # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)]  # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:  # 이미 깊이를 구했다면 -> 넘기기
            continue
        parent[y][0] = x  # 2^0 위 = 한 칸 위에 있는 부모에 대한 정보만 먼저 기록
        dfs(y, depth + 1)


# 모든 노드의 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1, 0)  # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n + 1):
            # parent[j][i-1] = j의 2^(i-1) 만큼 위에 있는 조상
            # A 정점의 2^1 번 째 조상노드 = A 정점의 2^0 번 째 조상노드의 2^0 번 째 조상노드
            # 처음에 2^0번 째(첫 번째 부모) 노드 값을 저장했다면 -> 아래의 점화식으로 각 노드들의 2^i 번째 부모 노드를 저장 가능
            # pre-order 로 순회하며 -> root 부터 top-down 으로 부모 노드를 채워 내려감 (각 최초의 부모 노드로 부터 그 노드의 부모노드를 기록함)
            parent[j][i] = parent[parent[j][i - 1]][
                i - 1
            ]  # 2의 제곱 꼴로 건너 뛰었을 때 부모를 기록 : 한 칸 앞에 있는 부모 -> 2칸 앞에 있는 부모 -> 4칸 앞에 있는 부모 -> 8칸 앞에 있는 부모 ..


# A 와 B 의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # b가 더 깊도록 설정 - 실제로 lca 함수를 호출할 때, 항상 b가 더 깊도록 SWAP 수행
    if d[a] > d[b]:
        a, b = b, a
    # 그 이후에 깊이(depth)가 동일하도록
    for i in range(LOG - 1, -1, -1):  # 큰 크기부터 -> 작은 크기까지 확인하며
        # 깊이 차이가 충분히 크다면 -> 2의 제곱꼴 만큼 감소하도록 하여 -> 더 깊은 쪽의 깊이가 줄어들 수 있도록 함
        # Ex) 깊이 차이가 15 였다면, 8 -> 4 -> 2 -> 1 로 줄어들도록 하여 4번만에 15 만큼 줄어들 수 있도록 함
        # 시프트 연산은 변수 << 이동할 비트 수 또는 변수 >> 이동할 비트 수 형식으로 사용
        if d[b] - d[a] >= (1 << i):  # 1 의 비트 값을 왼쪽으로 i 번 이동
            b = parent[b][i]

        # 더 깊은 a를 2승씩 점프하며 두 노드의 depth를 맞춘 후, 맞춘 depth의 조상 노드로 대체한다.
        # for (int i = K - 1; i >= 0; i--) {
        #     if (Math.pow(2, i) <= depth[a] - depth[b]) {
        #         a = parents[a][i]; // a를 2^i 번 째 조상 노드로 대체한다.
        #     }
        # }

    # 부모가 같아지도록
    # 부모가 같다면 -> 리턴
    if a == b:
        return a
    # 부모가 같지 않다면 -> 2의 제곱 형태에서, 큰 값 부터 -> 작은 값까지 확인해가며 거슬러 올라가도록
    # 예를 들어, 9칸 위로 올라갔을 때 만날 수 있다면, 8칸 이동했다가 -> 그 다음 1칸 이동
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]


set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
