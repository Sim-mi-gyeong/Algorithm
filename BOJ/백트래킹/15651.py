# N과 M(3)

n, m = map(int, input().split())
lst = []

def dfs():
    if len(lst) == m:
        s = ' '.join(map(str, lst))
        print(s)
        return   # 조건에 맞는 경우 현재 호출된 재귀함수를 return 하고 이전 재귀함수의 반복문으로 넘어가 실행

    for i in range(1, n+1):
        lst.append(i)
        dfs()
        lst.pop()
dfs()