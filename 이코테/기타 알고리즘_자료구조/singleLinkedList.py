class Node:
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer  # 노드의 오른쪽 포인터


class LinkedList:
    def __init__(self):
        self.head = None  # 연결 리스트의 첫 번째 원소
        self.length = 0  # 연결 리스트의 길이 저장

    # head 가 존재하는 경우 False, 존재하지 않는 경우 True 반환
    def is_empty_head(self):
        return not bool(self.head)

    # 가장 앞에 새로운 원소 추가
    def add_first(self, item):
        node = Node(item)
        if self.is_empty_head():  # head 노드가 존재하지 않는 경우
            self.head = node
        else:
            node.pointer = self.head
            self.head = node
        self.length += 1

    # 가장 뒤에 새로운 원소 추가
    def add_last(self, item):
        if self.is_empty_head():
            self.head = Node(item)
        else:
            node = self.head
            while node.pointer:
                node = node.pointer
            node.pointer = Node(item)
        self.length += 1

    # 새로운 원소 삽입
    def insert(self, pos, item):
        if self.is_empty_head():
            print("List is empty")
        # 처음 시작 위치는 0 (pos = 0 : 맨 앞에 삽입하는 경우)
        else:
            if pos == 0:
                self.add_first(item)
            elif pos == self.length:
                self.add_last(item)
            else:
                node = self.head  # 시작 노드부터 Count 세기
                cnt = 0
                while pos > 0 and pos < self.length:
                    # if) pos = 2 인 경우, 기존 연결리스트에서 2번째와 3번째 노드 사이에 삽입하고자 하는 경우
                    if cnt == pos - 1:
                        # 새로운 노드가 가리킬 pointer 노드는 = 이전 노드가 가리키던 pointer 노드
                        new_node = Node(item, node.pointer)
                        # 삽입할 위치 이전 노드가 새로운 노드를 가리키도록
                        node.pointer = new_node
                        break
                    # 다음 반복을 위해 다음 노드로
                    node = node.pointer
                    cnt += 1

                self.length += 1

    # target 노드 제거
    def remove(self, target):

        if self.is_empty_head():
            print("List is empty")
            return False
        else:
            node = self.head
            if node.value == target:
                self.head = node.pointer
                self.length -= 1
                return True
            else:
                # 삭제할 target 노드는 head 다음의 노드이고, 현재 node 에는 head 가 저장되어 있으니
                # prev 에 처음 저장하는 노드는 삭제할 노드의 이전 노드(head) 가 저장
                # node 에 처음 저장하는 노드는, head 노드가 가리키는 노드 (target 의 후보가 되는 노드)
                prev = node
                node = node.pointer
                while node:
                    if node.value == target:
                        prev.pointer = node.pointer
                        node = None
                        self.length -= 1
                        return True
                    prev = node
                    node = node.pointer
                return False

    # target 을 입력받아 -> 연결리스트에서 target 의 pos 를 반환
    # target 이 연결리스트 안에 존재하면 pos 를, 없으면 False 를 반환
    def search_target(self, target):
        if self.is_empty_head():
            print("List is empty")
            return False
        else:
            pos = 0
            node = self.head
            while node:
                if node.value == target:
                    return pos
                node = node.pointer
                pos += 1
            return False

    # pos 를 입력받아 -> 연결리스트에서 pos 에 해당하는 값을 반환
    # 첫 번째 원소의 pos 는 0 이라고 한다.
    def search_pos(self, pos):
        if self.is_empty_head():
            print("List is empty")
            return False
        else:
            node = self.head
            cnt = 0
            while node:
                if cnt == pos:
                    return node.value
                node = node.pointer
                cnt += 1
            return False

    # 연결리스트의 크기를 반환
    def size(self):
        return self.length

    # 연결 리스트 노드의 값 출력
    def print(self):
        if self.is_empty_head():
            print("List is empty")
        else:
            node = self.head
            while node:
                print(node.value, end=" ")
                node = node.pointer
            print()


list = LinkedList()
list.add_last(5)
print("size is : ", list.size())
list.print()

list.add_last(9)
print("size is : ", list.size())
list.print()

list.add_first(3)
print("size is : ", list.size())
list.print()

list.insert(2, 7)
print("size is ", list.size())
list.print()

list.insert(0, 8)
print("size is ", list.size())
list.print()

list.remove(8)
print("size is ", list.size())
list.print()
