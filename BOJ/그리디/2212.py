# 센서

n = int(input())
k = int(input())
lst = list(map(int, input().split()))
lst.sort()
diff = []

for i in range(n - 1):
    diff.append(lst[i + 1] - lst[i])

diff = sorted(diff, reverse=True)

for i in range(k - 1):
    if i > len(diff) - 1:
        continue
    diff[i] = 0

print(sum(diff))
