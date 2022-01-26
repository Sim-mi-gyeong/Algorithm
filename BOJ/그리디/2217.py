# 로프
import sys
n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
lst.sort(reverse=True)
# ans = []
# i = 1
# while (i != len(lst)):
#     cnt = 10000
#     target = lst[:i]
#     for j in target:
#         cnt = min(cnt, i * j)
#     ans.append(cnt)
#     if cnt < ans[-1]: break
#     else: i += 1
# print(max(ans))
ans = 0
for i in range(n):
    ans = max(ans, lst[i] * (i+1))
print(ans)