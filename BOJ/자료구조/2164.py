# 카드2

from collections import deque
n = int(input())
queue = deque([i for i in range(1, n+1)])

while (len(queue) != 1):
    queue.popleft()    # 제일 앞에 있는 카드 버리고
    v = queue.popleft()   # 그 다음 앞의 카드를 꺼내
    queue.append(v)   # 가장 뒤에 추가
    if len(queue) == 1: break
print(queue.popleft())