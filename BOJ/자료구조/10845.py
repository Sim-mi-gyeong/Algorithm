# 큐

from collections import deque
import sys
queue = deque([])
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        queue.append(s[1])
    if s[0] == 'front':
        if len(queue) == 0: print(-1)
        else: print(queue[0])
    if s[0] == 'pop':
        if len(queue) == 0: print(-1)
        else: print(queue.popleft())
    if s[0] == 'size': print(len(queue))
    if s[0] == 'back':
        if len(queue) == 0: print(-1)
        else: print(queue[-1])
    if s[0] == 'empty':
        if len(queue) == 0: print(1)
        else: print(0)