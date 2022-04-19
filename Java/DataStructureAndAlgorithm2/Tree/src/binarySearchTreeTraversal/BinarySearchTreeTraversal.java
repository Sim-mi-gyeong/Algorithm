package binarySearchTreeTraversal;

class Node {
    private int data;
    private Node left;
    private Node right;

    public Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
    public int getData() {
        return data;
    }
    public void setData(int data) {
        this.data = data;
    }
    public Node getLeft() {
        return left;
    }
    public void setLeft(Node left) {
        this.left = left;
    }
    public Node getRight() {
        return right;
    }
    public void setRight(Node right) {
        this.right = right;
    }

}
class TreeClass {   // 단순히 데이터와 좌우 자식노드만 지정해주도록
    private Node newNode;

    public Node buildNode(int data, Node left, Node right) {
        newNode = new Node(data);
        newNode.setLeft(left);
        newNode.setRight(right);

        return newNode;
    }
    // TODO 전위 순회
    public void preOrder(Node node) {
        if (node != null) {
            System.out.print(node.getData() + " ");
            preOrder(node.getLeft());
            preOrder(node.getRight());
        }
    }
    // TODO 중위 순회
    public static void inOrder(Node node) {
        if (node != null) {
            inOrder(node.getLeft());
            System.out.print(node.getData() + " ");
            inOrder(node.getRight());
        }
    }
    // TODO 후위 순회
    public static void postOrder(Node node) {
        if (node != null) {
            postOrder(node.getLeft());
            postOrder(node.getRight());
            System.out.print(node.getData() + " ");
        }
    }

}

public class BinarySearchTreeTraversal {
    public static void main(String[] args) {
        TreeClass tc = new TreeClass();

        Node n50 = tc.buildNode(50, null, null);
        Node n60 = tc.buildNode(60, null, null);
        Node n20 = tc.buildNode(20, n50, n60);
        Node n30 = tc.buildNode(30, null, null);
        Node n10 = tc.buildNode(10, n20, n30);   // root 노드는 n10

        /**
         *       10
         *     /    \
         *    20    30
         *   /  \
         *  50  60
         */
        System.out.print("전위 순회 결과 : ");
        tc.preOrder(n10);
        System.out.println();
        System.out.print("중위 순회 결과 : ");
        tc.inOrder(n10);
        System.out.println();
        System.out.print("후위 순회 결과 : ");
        tc.postOrder(n10);

    }
}
