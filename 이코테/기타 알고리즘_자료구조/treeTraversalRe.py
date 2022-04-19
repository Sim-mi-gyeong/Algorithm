# 트리 순회


class Node:
    def __init__(self, data, left_node, right_node):  # data : 자신의 데이터를 명시 -> left와 right 명시
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


# 전위 순회(Preorder Traversal) - 자신의 데이터를 먼저 처리한 뒤 -> 왼쪽 자식과 오른쪽 자식 처리
def pre_order(node):
    print(node.data, end=" ")  # 자기 자신 먼저 출력
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])


# 중위 순회(Inorder Traversal) - 왼쪽을 먼저 방문한 뒤 -> 자기 자신을 방문 처리하고 -> 오른쪽 자식 방문 처리
def in_order(node):
    # 왼쪽 자식 노드로 이동 먼저
    if node.left_node != None:
        in_order(tree[node.left_node])  # 처음 함수 호출 시 파라미터로 전달된 노드의 왼쪽 자식 노드가 이제 자기 자신이 됨
    print(node.data, end=" ")  # 더 이상 왼쪽 자식이 없는 경우, 자기 자신 출력 -> 재귀 빠져나가는(이전 호출 함수로) 형태
    if node.right_node != None:
        in_order(tree[node.right_node])


# 후위 순회(Postorder Traversal) - 왼쪽을 먼저 방문한 뒤 -> 오른쪽을 방문하고 -> 마지막을 자기 자신 방문 처리
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=" ")


n = int(input())
tree = {}

for _ in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None

    tree[data] = Node(data, left_node, right_node)  # 이진 트리 구성


pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])


# print(tree)
"""
{'A': <__main__.Node object at 0x7fd18009ec10>, 'B': <__main__.Node object at 0x7fd19003b1c0>, 
 'C': <__main__.Node object at 0x7fd19003b3a0>, 'D': <__main__.Node object at 0x7fd19003b2e0>, 
 'E': <__main__.Node object at 0x7fd19003b220>, 'F': <__main__.Node object at 0x7fd19003b6a0>, 
 'G': <__main__.Node object at 0x7fd19003b550>}
"""


"""
[예시 입력]
- 입력은, 노드의 개수 -> 하나의 노드와 각 노드에 연결된 자식노드를 split 하여 입력
7
A B C
B D E
C F G
D None None
E None None
F None None
G None None
[예시 출력]
A B D E C F G 
D B E A F C G 
D E B F G C A 
"""

"""
7
A B C
B D None
C E F
E None None
F None G
D None None
G None None
"""
