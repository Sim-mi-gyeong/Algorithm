package binarySearchTree.binarySearchTreeCal;
// 이진 탐색 트리 연산(찾기/삽입/삭제)
class Node {
    private int data;   // 자기 자신
    private Node left;   // 왼쪽 자식 노드
    private Node right;   // 오른쪽 자식 노드

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

public class BinarySearchTree {
    public static Node root;

    /**
     * find(탐색) 연산 : 이진 탐색 트리는 동일한 노드 값 X
     * 이진 탐색 트리의 삽입/삭제 연산은 '탐색' 과정을 거친 후 이루어짐
     * "왼쪽 자식 노드의 값 < 현재 노드의 값" & "현재 노드의 값 < 오른쪽 자식 노드의 값"
     */
    public boolean find(int value) {   // value = 찾고자 하는 값
        Node currentNode = root;
        while (currentNode != null) {
            if (currentNode.getData() == value) {
                return true;   // 현재 노드 = 찾는 값
            } else if (currentNode.getData() > value) {   // 찾는 값 < 현재 노드의 값 -> 왼쪽 자식 노드로
                currentNode = currentNode.getLeft();
            } else {   // 찾는 값 > 현재 노드의 값 -> 오른쪽 자식 노드로
                currentNode = currentNode.getRight();
            }
        }
        return false;
    }

    /**
     * insert(삽입) 연산
     */
    public boolean insert(int value) {
        Node newNode = new Node(value);   // 값을 받아 새로운 newNode 생성
        if (find(value)) {
            return false;
        }
        // 로트 노드가 없는 경우, 즉 트리가 비어있는 상태일 때 -> newNode 를 root 로 변경
        // - 처음 값을 insert 할 경우, root 가 null 인 상태 -> 새로 생성한 newNode 를 root 로
        // - 다음 값을 insert 할 때는, root 가 이미 존재하는 상황 -> currentNode = root(이전에 삽입한 값) 그대로
        if (root == null) {
            root = newNode;
            return true;
        }
        Node currentNode = root;
        Node parent;

        while (true) {
            parent = currentNode;
            if (value < currentNode.getData()) {   // insert 하려는 값 < 현재 노드의 값 -> 현재 노드의 왼쪽 자식으로 이동
                currentNode = currentNode.getLeft();
                if (currentNode == null) {   // 현재 노드의 왼쪽 자식 노드가 비어있는 상태이면, 즉 값이 없는 상태이면 -> 여기에 insert
                    parent.setLeft(newNode);
                    return true;
                }
            } else {   // insert 하려는 값 > 현재 노드의 값 -> 현재 노드의 오른쪽 자식으로 이동
                currentNode = currentNode.getRight();
                if (currentNode == null) {
                    parent.setRight(newNode);   // 더 이상 (오른쪽) 자식 노드가 없는 경우 -> insert
                    return true;
                }
            }
        }
    }

    /**
     * delete(삭제) 연산 - 삭제 후 이진 탐색 트리 구조를 다시 만들어야 함!
     * - 즉, 삭제하는 값(기준)에 따라 삭제 연산 과정이 달라짐
     * -> case 를 나누어 연산 시행
     * 1. (삭제하고자 하는 노드가) 자식 노드가 없는 경우 : 해당 노드 삭제 => 부모 노드의 참조값 삭제
     * 2. 자식 노드가 하나인 경우 : 부모 노드의 자식 노드를 => 삭제하려는 노드의 자식 노드로 대체 -> 삭제하고자 하는 노드 제거
     * 3. 자식 노드가 두 개인 경우 - 둘 중 하나로 기준을 잡아 처리
     *  3-1. 삭제 노드의 '좌측 최댓값' 을 올림
     *  3-2. 삭제 노드의 '우측 최솟값' 을 올림
     */
    public boolean delete(int value) {
        Node parentNode = root;    // 삭제하고자 하는 노드의 부모 노드
        Node currentNode = root;
        boolean isLeftChild = false;   // 삭제하고자 하는 노드가 현재 노드 기준 왼쪽/오른쪽 인지 확인

        // 현재 노드의 값이 삭제하고자 하는 값이 아닌 경우 -> 즉, 삭제하고자 하는 값을 찾을 때까지
        while (currentNode.getData() != value) {
            // TODO parentNode = 삭제하고자 하는 값의 위치를 찾기 위해 내려가기 전의 값을 저장
            //  -> 반복문 종료 후에는 삭제하고자 하는 값의 바로 위 부모 노드가 저장된 상태
            parentNode = currentNode;
            if (currentNode.getData() > value) {   // 현재 노드 값 > 삭제할 노드의 값 -> 왼쪽 자식이 존재하는 것 -> 현재 노드으 왼쪽 자식 노드로 이동
                isLeftChild = true;   // 삭제할 노드가 현재 노드의 왼쪽
                currentNode = currentNode.getLeft();
            } else {
                isLeftChild = false;
                currentNode = currentNode.getRight();
            }
            if (currentNode == null) {
                return false;   // 위에서 이동해온 온 노드의 값이 null 이면, 즉 존재하지 않으면
            }
        }
        // 위의 반복문을 거친 후 currentNode = 삭제하고자 하는 노드가 된 상태
        // TODO 1. 자식 노드가 없는 경우 - 해당 노드 삭제 & 부모 링크 삭제
        if (currentNode.getLeft() == null && currentNode.getRight() == null) {
            if (currentNode == null) {   // 해당 노드(삭제하고자 하는 노드)가 루트 노드인 경우, 즉 트리에 노드가 하나만 존재하는 경우
                root = null;
            }
            if (isLeftChild) {
                parentNode.setLeft(null);
            } else {
                parentNode.setRight(null);
            }
            return true;
        }

        // TODO 2-1. 자식 노드가 하나인 경우(왼쪽 자식만 존재)
        else if (currentNode.getRight() == null) {
            parentNode.setLeft(currentNode.getLeft());
        }

        // TODO 2-2. 자식 노드가 하나인 경우(오른쪽 자식만 존재)
        else if (currentNode.getLeft() == null) {
            parentNode.setRight(currentNode.getRight());
        }

        // TODO 3. 자식 노드가 둘인 경우
        else {
            Node minimum = getMinimum(currentNode);
            if (currentNode == root) {   // 삭제하려고 하는 노드가, root 인 경우 -> 루트 값을 minimum 으로 대체
                root = minimum;   //
            } else if (isLeftChild) {   // 왼쪽 자식 노드를 삭제하려고 하는 경우
                parentNode.setLeft(minimum);   // 삭제하려고 하는 노드의 부모 노드의 왼쪽 자식(삭제 노드)를 => minimum 으로 대체
            } else {   // 오른쪽 자식 노드를 삭제하려고 하는 경우
                parentNode.setRight(minimum);   // 삭제하려고 하는 노드의 부모 노드의 오른쪽 자식(삭제 노드)를 => minimum 으로 대체
            }
            minimum.setLeft(currentNode.getLeft());

        }

        return true;   // 위에서 존재하지 않으면 return false 처리 되므로 삭제 성공 시 return true
    }
    // TODO 3-3. 자식 노드가 2개인 경우
    //  -> 자식 노드 중에서 '삭제할 노드보다 크면서' & '가장 작은 값'을 삭제하는 경우
    //  -> 삭제할 노드의 오른쪽 서브트리의 최솟값 찾기
    //  -> 이 값으로 삭제하고자 하는 값을 제거 후 남는 빈자리 채우기
    public static Node getMinimum(Node deleteNode) {   // deleteNode = currentNode
        Node minimum = null;
        Node minimumParent = null;
        Node currentNode = deleteNode.getRight();   // 삭제하고자 하는 노드의 오른쪽 노드로 이동 -> 존재하지 않을 때까지 계속 이동
        while (currentNode != null) {   // 삭제하고자 하는 노드의 '오른쪽 서브트리' 에서 '왼쪽 노드' 로 계속 이동해서 null 이 나올 때까지
            // TODO ??
            minimumParent = minimum;   // minimum 의 부모 노드 정보 저장 -> 이후 minimum 은 이전 반복문에서 수행된 currentNode 의 getLeft() 값으로 업데이트
            minimum = currentNode;
            currentNode = currentNode.getLeft();
        } // while 문을 빠져나온 상태에서는 currentNode 가 이 메서드 내에서 null
        if (minimum != deleteNode.getRight()) {
            minimumParent.setLeft(minimum.getRight());   // minimum 의 왼쪽 자식 노드 = 원래 minimum => minimum 의 오른쪽 노드로 대체 (minimum의 왼쪽 노드보다는 값이 커야 하므로)
            minimum.setRight(deleteNode.getRight());   // minimum 이 삭제하려고 하던 노드의 자리로 가므로 -> minimum 의 오른쪽 자식 => 삭제하려고 하던 값의 원래 오른쪽 자식 노드로
        }

        return minimum;
    }
    // TODO 3-3. 자식 노드가 2개인 경우
    //  -> 자식 노드 중에서 '삭제할 노드보다 작으면서' & '가장 큰 값'을 삭제하는 경우
    //  -> 삭제할 노드의 왼쪽 서브트리의 최댓값 찾기
    //  -> 이 값으로 삭제하고자 하는 값을 제거 후 남는 빈자리 채우기
    public static Node getMaximum(Node deleteNode) {
        Node maximum = null;
        Node maximumParent = null;
        Node currentNode = deleteNode.getLeft();

        while(currentNode != null) {
            maximumParent = maximum;   // maximum 의 부모 노드 정보 저장 -> 이후 maximum 은 이전 반복문에서 수행된 currentNode 의 getRight() 값으로 업데이트
            maximum = currentNode;
            currentNode = currentNode.getRight();
        }
        if (maximum != deleteNode.getLeft()) {
            maximumParent.setRight(maximum.getLeft());
            maximum.setLeft(deleteNode.getLeft());
        }

        return maximum;
    }

    // TODO 전위 순회
    public static void preOrder(Node node) {
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

    public static void main(String[] args) {

        BinarySearchTree bst = new BinarySearchTree();

        int[] arr = {5, 2, 1, 3, 7, 4, 6, 8};
        for (int x: arr) bst.insert(x);
        // 이진 탐색 트리에서 6 찾기
        int targetNum = arr[6];
        if (bst.find(targetNum)) {
            System.out.println("이진 탐색 트리에서 " + targetNum + " 찾음 !!");
        } else {
            System.out.println("이진 탐색 트리에서 " + targetNum + " 찾지 못 함 !!");
        }

        int deleteNum = 7;
        System.out.print("이진 탐색 트리 삭제 연산 전 : ");
        for (int x: arr) System.out.print(x + " ");
        System.out.println();
        if (bst.delete(deleteNum)) {
            System.out.println("이진 탐색 트리 삭제 연산 성공");
//            System.out.print("이진 탐색 트리 삭제 연산 후 : ");   // 5 2 8 1 3 6 4
//            for (int x: arr) System.out.print(x + " ");
            System.out.print("삭제 연산 후 전위 순회 결과 : ");
            preOrder(root);
//            System.out.println(preOrder(root));   // 전위/중위/후위 순회로 출력하도록

        }
    }
}
