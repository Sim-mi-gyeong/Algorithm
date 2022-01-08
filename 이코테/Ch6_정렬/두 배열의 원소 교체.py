n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]:   # A의 원소가 B의 원소보다 작은 경우에만 교체
        a[i], b[i] = b[i], a[i]
print(sum(a))