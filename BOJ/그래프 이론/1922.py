# 네트워크 연결

n = int(input())
m = int(input())

# 노드 정보 입력 받아 비용 기준 오름차순 정렬
edge = []
for i in range(m):
    a, b, cost = map(int, input().split())
    edge.append([a, b, cost])
edge.sort(key = lambda x : x[2])

# 부모 테이블 세팅 및 부모 찾기 위한 연산
parent = [0] * (n + 1)
for i in range(1, n+1): parent[i] = i
def findParent(x, parent):
    if parent[x] == x:   # 자기 자신과, 부모 테이블에서 자기 자신에 해당하는 인덱스의 값이 같다면
        return x
    else:   # 다르다면, 조상 부모(부모의 부모, 부모의 ~ ..)를 찾기 위한 함수 다시 호출
        parent[x] = findParent(parent[x], parent)
    return parent[x]

# Union 연산 - 사이클이 발생하지 않을 때, 부모 원소를 더 작은 원소의 값으로 대체하기 위한 연산
def union(a, b, parent):
    a = findParent(a, parent)
    b = findParent(b, parent)
    # a 의 부모 원소가 더 작은 경우, b 의 부모 원소를 a 의 부모 원소로 대체
    if a < b: parent[b] = a 
    else: parent[a] = b

# 사이클 발생 여부 체크 - 부모가 같은지/다른지 확인
# -> 다르다면 Union 연산으로 비교해 부모 값을 더 작은 값으로
total = 0
for a, b, cost in edge:
    # 부모가 같지 않으면 -> 최소 스패닝 트리에 포함 -> union 연산
    if findParent(a, parent) != findParent(b, parent):
        union(a, b, parent)
        total += cost
    # 부모가 같은 경우 -> 최소 스패낭 트리에 포함 X

print(total)