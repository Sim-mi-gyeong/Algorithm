# N과 M(4)
# 시간 초과

# 같은 수 출력 가능, '비'내림차순
# sort 의 비효율성 -> 이전의 idx 값을 넘겨주어, idx 이하는 진행하지 않도록

n, m = map(int, input().split())
lst = []
dupli = []
def dfs():
    if len(lst) == m: 
        
        tmp = tuple(sorted(lst))
        if tmp not in dupli:
            s = ' '.join(map(str, tmp))
            dupli.append(tmp)
            print(s)
        return
    
    for i in range(1, n+1):
        lst.append(i)
        dfs()
        lst.pop()
dfs()