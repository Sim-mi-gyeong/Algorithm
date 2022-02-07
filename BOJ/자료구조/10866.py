# 덱

import sys
from collections import deque
deq = deque()

n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().split()

    if s[0] == 'push_front': deq.appendleft(s[1])
    elif s[0] == 'push_back': deq.append(s[1])
    elif s[0] == 'pop_front':
        if len(deq) == 0: print(-1)
        else: print(deq.popleft())
    elif s[0] == 'pop_back':
        if len(deq) == 0: print(-1)
        else: print(deq.pop())
    elif s[0] == 'size': print(len(deq))
    elif s[0] == 'empty':
        if len(deq) == 0: print(1)
        else: print(0)
    elif s[0] == 'front':
        if len(deq) == 0: print(-1)
        else: print(deq[0])
    elif s[0] == 'back':
        if len(deq) == 0: print(-1)
        else: print(deq[-1])