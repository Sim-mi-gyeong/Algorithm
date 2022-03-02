# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v+1)
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 사이클 발생 여부
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우, 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않으면, 합집합(Union) 연산 수행
    else: union_parent(parent, a, b)

if cycle: print('사이클이 발생')
else: print('사이클 미발생')