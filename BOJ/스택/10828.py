# 스택

import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    a = list(sys.stdin.readline().split())
    b = a[0]
    if b == 'push':
        stack.append(a[1])
    elif b == 'top':
        if len(stack) == 0: print(-1)
        else: print(stack[-1])
    elif b == 'size':
        print(len(stack))
    elif b == 'pop':
        if len(stack) == 0: print(-1)
        else:
            print(stack.pop())    
    elif b == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)