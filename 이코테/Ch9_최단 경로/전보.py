# 통로는 방향성이 있는 간선

# 도시의 개수, 통로의 개수, 메시지 보내고자 하는 도시
n, m, c = map(int, input().split())
edge = []
for i in range(m):
    x, y, z = map(int, input().split())
    edge.append([x, y, z])
print(edge)