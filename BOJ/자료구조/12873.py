# 기념품
from collections import deque

n = int(input())
q = deque([i for i in range(1, n + 1)])
currStep = 1
currIdx = 0
remain_n = n
while len(q) > 1:
    tmpT = currStep ** 3 % len(q)

    if tmpT == 0:
        tmpT = len(q)

    for _ in range(tmpT - 1):
        head = q.popleft()
        q.append(head)

    q.popleft()
    currStep += 1

print(q[0])
