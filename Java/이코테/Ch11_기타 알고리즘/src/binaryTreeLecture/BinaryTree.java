package binaryTreeLecture;

class Node {
    private int value;   // 데이터
    private Node left;   // 왼쪽 서브트리 포인터
    private Node right;   // 오른쪽 서브트리 포인터

    public Node(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    public int getValue() {
        return value;
    }

    public Node getLeft() {
        return left;
    }

    public Node getRight() {
        return right;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public void setLeft(Node left) {
        this.left = left;
    }

    public void setRight(Node right) {
        this.right = right;
    }
}

public class BinaryTree {
    public Node root;

    // TODO find - Binary Tree는 동일한 Value가 존재하지 않으므로 존재 여부를 찾아야 함.
    public boolean find(int value) {
        Node currentNode = root;
        while (currentNode != null) {
            // 현재 노드와 찾는 값이 같은 경우 -> true
            if (currentNode.getValue() == value) {
                return true;
            // 찾는 값이 현재 노드보다 작다면,
            } else if (currentNode.getValue() > value) {
                currentNode = currentNode.getLeft();
            // 찾는 값이 현재 노드보다 크다면,
            } else {
                currentNode = currentNode.getRight();
            }
        }
        return false;
    }

    // TODO insert
    public boolean insert(int value) {
        Node newNode = new Node(value);   // 값을 받아 -> 새로운 New Node 생성
        // 처음 값을 삽입할 때, find 호출을 하면
        // Node 클래스를 찹조하는 root node 값이 할당되지 X => null
        // find(value);
        // System.out.println("root : " + root);
        // -> 현재 노드에 대한, Node 클래스를 참조하는 currentNode = root = null -> currentNode = null 이므로, while 문 통과 X
        // System.out.println("find(value) : " + find(value)); => false 반환
        if (find(value)) {
            return false;
        }
        // 처음 값을 insert 할 때 root 가 null -> root = value 가 24인 newNode -> 이 값을 root 로
        // 다음 값을 insert 할 때는 root 는 이미 값이 존재하는 상황 -> currentNode = root (이전 삽입한 값) 그대로
        // -> parent = 처음 insert 한 값
        System.out.println("newNode : " + newNode.getValue());
        if (root == null) {
            root = newNode;
            return true;
        }
        // find(value) 했을 때 -> 값이 존재하지 않고,
        // root 노드를 새로 생성한 New Node(value = 24) 로 설정한 경우
        Node currentNode = root;
        Node parent;
        // TODO currentNode 값을 찾기/삽입/삭제 하기 위해 이동하여 도달한 값
        while (true) {
            parent = currentNode;
            System.out.println("currentNode : " + currentNode.getValue());
            System.out.println("parent : " + parent.getValue());
            System.out.println("--------------------------------------");
            if (value < currentNode.getValue()) {   // 삽입하고자 하는 value 가, 현재 노드(부모)의 값보다 작다면 -> 왼쪽 노드
                currentNode = currentNode.getLeft();   // 왼쪽 노드로 이동
                if (currentNode == null) {   // 왼쪽 노드 값이 null 인 경우 -> 부모의 왼쪽 노드 값을 새로 insert 하는 값, 그 노드로
                    parent.setLeft(newNode);
                    return true;
                }
            } else {
                currentNode = currentNode.getRight();   // 현재, 부모의 왼쪽 노드로 이동
                if (currentNode == null) {
                    parent.setRight(newNode);
                    return true;
                }
            }
        }

    }

    // TODO delete
    /**
     * 삭제하고자 하는 값(기준) 에 따라 달라짐
     * -> 자식 노드들의 존재/개수 여부
     * 1. 자식이 없는 경우 : 해당 노드 삭제 -> 부모 노드의 참조값 삭제
     * 2. 자식이 하나인 경우 : '부모 노드(24)의 자식 노드를 => 해당 노드의 자식 노드(27)로 대체' -> 해당 노드(32) 삭제
     * 3. 자식이 2개인 경우
     *  - 둘 중 하나로 기준 잡아 처리
     *   1) 삭제 노드의 '좌측 최댓값' 을 올림
     *   2) 삭제 노드의 '우측 최솟값' 을 올림
     */
    public boolean delete(int value) {
        Node parentNode = root;
        Node currentNode = root;
        boolean isLeftChild = false;   // 왼쪽 자식 노드 존재 여부를 false 로 설정

        // 현재 위치한 노드가 삭제하고자 하는 값이 아니라면, 즉 루트 노드를 삭제하는 것이 아니라면
        while (currentNode.getValue() != value) {
            parentNode = currentNode;
            if (currentNode.getValue() > value) {   // 현재 노드 값 > 삭제할 노드 값 -> 현재 노드에서 왼쪽으로 이동
                isLeftChild = true;
                currentNode = currentNode.getLeft();   // 루트 노드의 왼쪽 자식 참조 값으로 현재 노드를 설정
            } else {
                isLeftChild = false;   // 현재 노드 값 < 삭제할 노드 값 -> 현재 노드에서 오른쪽으로 이동
                currentNode = currentNode.getRight();
            }
            if (currentNode == null) {   // 이동해서 온 노드 위치가 null 값이라면
                return false;
            }

        }

        // TODO 1. 자식 노드가 없는 경우


        // TODO 2-1. 자식 노드가 하나인 경우(왼쫀 자식만 존재)


        // TODO 2-2. 자식 노드가 하나인 경우(오른쪽 자식만 존재)


        // TODO 3. 자식 노드가 둘인 경우


        return false;
    }

    Node getMin(Node deleteNode) {
        Node minNode = null;
        Node minNodeParent = null;
        Node currentNode = deleteNode.getRight();
        return minNode;
    }


    // TODO print Node
    private void printNode() {
    }

    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();

        int[] arr = {24, 16, 11, 21, 32, 27};
        for (int i = 0; i < arr.length; i++) {
            tree.insert(arr[i]);
        }
        tree.delete(21);
        if (tree.find(21)) {
            System.out.println("binary Tree 에서 21 을 찾음 !");
        } else {
            System.out.println("binary Tree 에서 21 을 못 찾음 !");
        }
//        tree.printNode();
    }

}
