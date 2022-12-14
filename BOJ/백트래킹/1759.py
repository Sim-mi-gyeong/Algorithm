# 암호 만들기
# 최소 한 개의 모음 + 최소 두 개의 자음
# 오름차순 정렬

l, c = map(int, input().split())
lst = list(input().split())
lst = sorted(lst)
tmp = ""
m = ("a", "e", "i", "o", "u")


def dfs(tmp, depth):
    if depth == l:
        return

    while len(tmp) < l:
        for i in range(len(lst)):
            tmp += lst[i]
