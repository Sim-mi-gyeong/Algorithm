# 좌표 정렬하기
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key = lambda x: (x[0], x[1]))
for i in lst: print(i[0], i[1])