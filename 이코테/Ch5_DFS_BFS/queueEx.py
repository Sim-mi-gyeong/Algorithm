from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()
# queue = deque()   # deque([])
# queue.append(graph[0][0])

# queue = deque([initial value])

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)   # 먼저 들어온 순서대로 출력
queue.reverse()   # 역순으로 바꾸기
print(queue)   # 나중에 들어온 원소부터 출력

# 리스트에서 pop 메서드를 통해 원소를 꺼낸 후 리스트 원소 인덱스를 재정렬 하는 과정에서 O(k) 만큼의 시간복잡도 발생