package binaryTree;

import java.util.List;

public class Solution {
    public static void main(String[] args) {
        BinaryTree binaryTree = new BinaryTree();
        binaryTree.insert(5);
        binaryTree.insert(1);
        binaryTree.insert(2);
        binaryTree.insert(6);
        binaryTree.insert(7);
        binaryTree.insert(10);
        binaryTree.insert(9);

        List<Integer> preOrderTraverse = binaryTree.traverse(binaryTree.root, BinaryTree.PRE_ORDER_TRAVERSE);
        System.out.println("전위 탐색 결과");
        System.out.println(preOrderTraverse);
        System.out.println();

        List<Integer> inOrderTraverse = binaryTree.traverse(binaryTree.root, BinaryTree.IN_ORDER_TRAVERSE);
        System.out.println("중위 탐색 결과");
        System.out.println(inOrderTraverse);
        System.out.println();

        List<Integer> postOrderTraverse = binaryTree.traverse(binaryTree.root, BinaryTree.POST_ORDER_TRAVERSE);
        System.out.println("후위 탐색 결과");
        System.out.println(postOrderTraverse);
        System.out.println();

        List<Integer> bfs = binaryTree.bfs(binaryTree.root);
        System.out.println("BFS(너비 우선 탐색) 결관");
        System.out.println(bfs);


    }
}
