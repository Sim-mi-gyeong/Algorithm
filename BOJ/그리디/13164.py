# 행복 유치원
n, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

diff = []
for i in range(n - 1):
    diff.append(lst[i + 1] - lst[i])

diff.sort(reverse=True)

for i in range(k - 1):
    if i > len(diff) - 1:
        continue
    diff[i] = 0
print(sum(diff))
