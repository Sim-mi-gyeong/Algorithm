import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict()
for _ in range(n):
    dic[input()] = 0

cnt = 0
for _ in range(m):
    s = input()
    if s in dic:
        cnt += 1
print(cnt)
