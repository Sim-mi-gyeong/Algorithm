# 경로 찾기
# 플로이드-워셜 알고리즘
# i 에서 -> j로 이동 시 k를 거쳐서 가는 경우 !! 다 표시

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):   # 정점
    for j in range(n):   # 행
        for k in range(n):   # 열
            if graph[j][i] == 1 and graph[i][k] == 1:
                graph[j][k] = 1
for i in graph:
    for j in i: print(j, end= ' ')
    print()