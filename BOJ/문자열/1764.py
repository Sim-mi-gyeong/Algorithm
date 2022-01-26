# 듣보잡
# 두 개의 리스트에서 중복되는 원소
n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
a.sort()
b.sort()
ans = []
for i in a:
    if i in b: ans.append(i)
ans.sort()
for i in ans: print(i)