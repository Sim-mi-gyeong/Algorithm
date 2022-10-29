class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    # 이중 연결리스트는 연결리스트의 시작을 나타내는 head 와 끝을 나타내는 tail 을 갖는다
    def __init__(self):
        self.head = None  # 연결리스트의 첫 번째 원소
        self.tail = self.head  # 연결리스트의 마지막 원소

    # 연결리스트가 비어있는지 확인
    def empty(self):
        return not bool(self.head)

    # 연결리스트의 마지막 위치에 새로운 노드 추가
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.tail
            new_node = Node(data, prev=node)
            node.next = new_node
            self.tail = new_node

    # 연결리스트의 첫 번째 위치에 새로운 노드 추가
    def append_left(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            new_node = Node(data, next=node)
            node.prev = new_node
            self.head = new_node

    # 특정 노드 이전에 노드 추가
    def insert_before(self, next_data, new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.tail = self.head
        else:
            node = self.tail
            while node.data != next_data:
                node = node.prev
                if node is None:  # 연결리스트의 가장 첫번째까지 탐색한 경우
                    return False

            # 찾으려는 값 next_data 를 찾은 경우 -> next_data 를 포함한 노드 앞에 new_data 를 포함한 노드 추가
            prev_node = node.prev
            new_node = Node(new_data, prev=prev_node, next=node)
            if prev_node:  # prev_node 가 Null 이 아닌 경우
                prev_node.next = new_node
            else:
                self.head = new_node
            node.prev = new_node
            return True

    # 특정 노드 이후에 노드 추가
    def insert_after(self, prev_data, new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.tail = self.head
        else:
            node = self.head
            while node.data != prev_data:
                node = node.next
                if node is None:  # 연결리스트의 가장 마지막까지 탐색한 경우
                    return False

            # 찾으려는 값 prev_data 를 찾은 경우 -> prev_data 를 포함한 노드 다음에 new_data 를 포함한 노드 추가
            next_node = node.next
            new_node = Node(new_data, prev=node, next=next_node)
            if next_node:
                next_node.prev = new_node
            else:
                self.tail = new_node
            node.next = new_node

    # 리스트의 마지막 값을 반환 - 리스트가 비었을 경우 IndexError
    def pop(self):
        if self.head is None:
            raise IndexError("LinkedList is empty")
        item = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return item

    # 리스트의 첫번째 값을 반환 - 리스트가 비었을 경우 IndexError
    def popleft(self):
        if self.head is None:
            raise IndexError("LinkedList is empty")
        item = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return item

    # 출력함수 - 리스트의 저장된 값을 string 으로 받아 result 에 저장 -> String 타입인 result 를 반환
    def __str__(self):
        node = self.head
        result = ""
        while node is not None:
            result += str(node.data) + " "
            node = node.next
        return result

    # 리스트 길이 반환 함수 - 리스트를 순환하면서 노드 당 cnt 값을 하나씩 증가시키고 -> cnt 값 반환
    def __len__(self):
        node = self.head
        cnt = 0
        while node is not None:
            cnt += 1
            node = node.next
        return cnt


DL = DoubleLinkedList()
DL.append(1)
DL.append(3)
DL.append(5)
print(DL)

DL.append_left(100)
print(DL)

DL.insert_after(1, 2)
print(DL)

DL.insert_before(5, 4)
print(DL)

print(len(DL))

DL.pop()
print(DL)

DL.popleft()
print(DL)

print(len(DL))
