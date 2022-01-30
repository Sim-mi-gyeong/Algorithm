# 프린터 큐

# test case 3번째와 같이 같은 수이지만 인덱스가 다른 수의 순서를 확인하기 위해 idx queue 필요

from collections import deque

n = int(input()) 
for i in range(n):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    idxQueue = deque(list(range(len(queue))))
    cnt = 0
    while queue:
        a = max(queue)
        v = queue[0]
        if v == a:
            queue.popleft()
            idx = idxQueue.popleft()
            cnt += 1
            if idx == m: break
        if v < a:   # 가장 앞의 원소가 최댓값이 아니라면,
            queue.append(queue.popleft())   # 해당 원소를 빼내서, 뒤로 넣기  
            idxQueue.append(idxQueue.popleft())   # 인덱스에 해당하는 queue도 동일하게
    print(cnt)