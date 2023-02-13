import sys

input = sys.stdin.readline

t = int(input().rstrip())
INF = 10001


def bellmanFord(start):
    distance = [INF] * (n + 1)
    distance[start] = 0

    for i in range(n):
        for j in range(len(edge)):
            currNode, nextNode, cost = edge[j][0], edge[j][1], edge[j][2]
            if distance[nextNode] > distance[currNode] + cost:
                distance[nextNode] = distance[currNode] + cost
                if i == n - 1:
                    return True
    return False


for _ in range(t):
    n, m, w = map(int, input().rstrip().split())
    edge = []

    for _ in range(m):
        s, e, t = map(int, input().rstrip().split())
        edge.append((s, e, t))
        edge.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().rstrip().split())
        edge.append((s, e, -t))

    check = bellmanFord(1)
    if check:
        print("YES")
    else:
        print("NO")
