# 최소 스패닝 트리

import sys
v, e = map(int, sys.stdin.readline().split())

# 부모 테이블 세팅
parent = [0] * (v+1)
for i in range(1, v+1): parent[i] = i
def find_parent(parent, x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 서로의 부모 원소를 비교해 작은 값으로 
    if a < b: parent[b] = a
    else: parent[a] = b

graph = []
total = 0
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph.append([a, b, cost])
# 비용 기준 오름차순 정렬
graph.sort(key = lambda x: x[2])

for i in range(len(graph)):
    a, b, cost = graph[i]
    # 사이클 발생 여부 체크 : 서로의 부모가 다른지 확인
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)   # 다르면, union 연산 수행 -> 최소 신장 트리 포함 
        total += cost
print(total)