# N과 M(4)
# sort 의 비효율성 -> 이전의 idx 값을 넘겨주어, idx 이하는 진행하지 않도록
# 이전에 중복 체크를 리스트에 추가, 존재 여부 확인으로 했다면 -> 방문 처리로 

n, m = map(int, input().split())
lst = []

def dfs(depth, idx):
    if depth == m:
        print(' '.join(map(str, lst)))
        return
    # 비내림차순을 위해 idx 적용 -> 재귀 호출 시 +1 한 수부터 반복문 처리 
    for i in range(idx, n):  
        lst.append(i+1)
        # 중복되는 수(1 1)와 같이, 이미 존재하는 같은 수를 고를 수 있도록 i+1 대신 i 넘겨주기
        dfs(depth + 1, i)
        lst.pop()
dfs(0, 0)