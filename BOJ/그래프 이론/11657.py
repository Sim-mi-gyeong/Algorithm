# 타임머신
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = []
d = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bellmanFord(start):
    d[start] = 0
    for i in range(n):  # 전체 n 번 반복 - m 개의 간선 모두 확인
        for j in range(m):
            currNode = edges[j][0]
            nextNode = edges[j][1]
            cost = edges[j][2]

            if d[currNode] != INF and d[currNode] + cost < d[nextNode]:
                d[nextNode] = d[currNode] + cost

                if i == n - 1:  # n 번 째에도 값이 갱신되는 경우 -> 음수 사이클
                    return True

    return False


negativeCyvle = bellmanFord(1)

if negativeCyvle:
    print(-1)  # 음수 간선 순환 -> 시간을 무한히 오래 전으로
else:
    for i in range(2, n + 1):
        if d[i] == INF:
            print(-1)
        else:
            print(d[i])
