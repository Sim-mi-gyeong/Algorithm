# 요세푸스 문제

from collections import deque
n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
ans = []

while queue:
    for i in range(k):   # n번 빼고 뒤로 넣고
        queue.append(queue.popleft())
    v = queue.pop()
    ans.append(v)   # 가장 뒤의 원소가 요세푸스 순열 요소

print('<', ', '.join(str(i) for i in ans)[:], '>', sep='')
# print('<', ', '.join(map(str, ans)), '>')