# 두 배열 원소 개수 최대 100,000개 -> 최악의 경우 O(NlonN) 보장히도록

n, k = map(int, input().split())  # 최대 k 번 교체 가능
a = list(map(int, input().split()))
b = list(map(int, input().split()))

maxValue = 0

a.sort()
b.sort(reverse=True)
cnt = 0
for i in range(len(a)):
    if a[i] < b[i]:
        if cnt < k:
            a[i], b[i] = b[i], a[i]
            cnt += 1
        elif cnt == k:
            break
    else:
        continue
    maxValue = max(maxValue, sum(a))
print(maxValue)

# for i in range(k):
#     if a[i] < b[i]:
#         a[i], b[i] = b[i], a[i]
#     else:
#         break
# print(sum(a))

"""
5 3
1 2 5 4 3
5 5 6 6 5
"""
