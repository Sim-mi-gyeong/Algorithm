# N과 M(2)

# 중복 체크를 lst 포함여부 대신 -> visited 로 방문처리 
# sort 대신 -> idx 를 넘겨 그 이하는 실행되지 못하도록
n, m = map(int, input().split())
lst = []

visited = [False] * n
def dfs2(depth, idx):
    if depth == m:
        print(' '.join(map(str, lst)))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            lst.append(i+1)
            dfs2(depth+1, i+1)
            visited[i] = False   # 백트래킹 -> 위에서 dfs 를 재귀 호출 했을 때 반복문 처리를 못하면, 이전 함수에서 백트래킹 수행
            lst.pop()
dfs2(0, 0)