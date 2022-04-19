# 트리 순회

import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data, leftNode, rightNode):
        self.data = data
        self.leftNode = leftNode
        self.rightNode = rightNode


# 전위 순회
def pre_order(node):
    print(node.data, end="")
    if node.leftNode != ".":
        pre_order(tree[node.leftNode])
    if node.rightNode != ".":
        pre_order(tree[node.rightNode])
    return


# 중위 순회
def in_order(node):
    if node.leftNode != ".":
        in_order(tree[node.leftNode])
    print(node.data, end="")
    if node.rightNode != ".":
        in_order(tree[node.rightNode])


# 후위 순회
def post_order(node):
    if node.leftNode != ".":
        post_order(tree[node.leftNode])
    if node.rightNode != ".":
        post_order(tree[node.rightNode])
    print(node.data, end="")


n = int(input())
tree = {}

for _ in range(n):
    data, leftNode, rightNode = input().split()
    # if leftNode == ".":
    #     leftNode = None
    # if rightNode == ".":
    #     rightNode = None

    tree[data] = Node(data, leftNode, rightNode)

print(pre_order(tree["A"]))
print(in_order(tree["A"]))
print(post_order(tree["A"]))
