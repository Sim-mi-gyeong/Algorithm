# 나이순 정렬
n = int(input())
s = [list(input().split()) for _ in range(n)]
s.sort(key=lambda x: int(x[0]))
for i in s: print(i[0], i[1])