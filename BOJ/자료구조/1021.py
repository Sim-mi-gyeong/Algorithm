# 회전하는 큐
from collections import deque

n, m = map(int, input().split())
lst = list(map(int, input().split()))
queue = deque([i for i in range(1, n+1)])
cnt = 0

for i in lst:
    if i == queue[0]:
        queue.popleft()
        continue

    else:   # Front 원소와 뽑아내고자 하는 원소가 같지 않으면
        while i != queue[0]:
            if queue.index(i) <= (len(queue) / 2):
                front = queue.popleft()
                queue.append(front)
            else:
                end = queue.pop()
                queue.appendleft(end)
            cnt += 1
        queue.popleft()

print(cnt) 