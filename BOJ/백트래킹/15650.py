# N과 M(2)

n, m = map(int, input().split())
lst = []
dupli = []

def dfs():
    if len(lst) == m:
        tmp = sorted(lst)
        if tmp not in dupli:   # 정렬을 한 것에 대해 중복 체크 먼저 후,
            dupli.append(tmp)
            s = ' '.join(map(str, tmp))
            print(s)

    for i in range(1, n+1):
        if i not in lst:
            lst.append(i) 
            dfs()
            lst.pop()
dfs()