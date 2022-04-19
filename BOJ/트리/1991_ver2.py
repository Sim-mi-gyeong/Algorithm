# 트리 순회

import sys

input = sys.stdin.readline


# 전위 순회
def pre_order(node):
    if node != ".":
        print(node, end="")
        pre_order(tree[node][0])
        pre_order(tree[node][1])


# 중위 순회
def in_order(node):
    if node != ".":
        in_order(tree[node][0])
        print(node, end="")
        in_order(tree[node][1])


# 후위 순회
def post_order(node):
    if node != ".":
        post_order(tree[node][0])
        post_order(tree[node][1])
        print(node, end="")


n = int(input())
tree = {}

for _ in range(n):
    data, leftNode, rightNode = input().split()
    tree[data] = [leftNode, rightNode]

pre_order("A")
print()
in_order("A")
print()
post_order("A")
