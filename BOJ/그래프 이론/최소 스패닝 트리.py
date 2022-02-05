# 참고 : https://techblog-history-younghunjo1.tistory.com/262

import sys
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v+1)
for i in range(1, v+1): parent[i] = i

# find 연산
def find_parent(parent, x):
    if parent[x] != x:   # 부모 원소가 자기 자신이 아니라면, 자기 자신을 자식으로 갖는 부모 원소를 찾기
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# uion 연산
def unio_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a   # 두 원소의 부모 원소를 비교해 작은 원소를 부모 원소로 설정
    else: parent[a] = b

# 간선 정보를 담을 리스트와, 최소 시장 트리 계산 변수 정의
edges = []
total_cost = 0

# 간선 정보가 주어지고, 비용 기준 오름차순 정렬
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort(key = lambda x : x[0])

# 간선 정보를 하나씩 확인하면서, 크루스칼 알고리즘 수행
for i in range(e):
    cost, a, b = edges[i]  
    # find 연산 후 부모 노드가 다르면 -> 사이클 발생하지 않음 
    # -> union 연산 수행 -> 최소 신장 트리에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        unio_parent(parent, a, b)
        total_cost += cost

print(total_cost)