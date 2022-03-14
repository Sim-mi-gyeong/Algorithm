package binaryTree;
// 이진트리 구현 - Insert
// 이진트리 탐색 방법(4가지) - 전위탐색(PreOrderTraversal), 중위탐색(inOrderTraversal), 후위탐색(PostOrderTraversal), 너비우선탐색(BFS)

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 3 가지 전제 조건
 *  1. 어떤 노드 N을 기준으로, 왼쪽 서브 트리 노드의 모든 키 값 < 노드 N의 키 값보다 작아야 함.
 *  2. 오른쪽 서브 트리 노드의 키 값 > 노드 N의 키 값보다 커야 함.
 *  3. 같은 키의 값을 갖는 노드는 존재하지 않음.
 *  -> 한 노드가 있을 때, 해당 노드보다 '작으면' => 왼쪽, '크면' => 오른쪽 으로 배치
 */

class Node {
    private Node left;
    private Node right;
    private int value;

    public Node(int value) {
        this.value = value;   // 노드가 갖는 실질적 데이터
        this.left = null;   // 노드의 왼쪽 자식
        this.right = null;   // 노드의 오른쪽 자식
    }
    public Node getLeft() {
        return left;
    }
    public Node getRight() {
        return right;
    }
    public int getValue() {
        return value;
    }
    public void setLeft(Node left) {
        this.left = left;
    }
    public void setRight(Node right) {
        this.right = right;
    }
    public void setValue(int value) {
        this.value = value;
    }

}

public class BinaryTree {

//    private class Node {
//        private Node left;
//        private Node right;
//        private int value;
//
//        public Node(int value) {
//            this.value = value;
//            this.left = null;
//            this.right = null;
//        }
//        public Node getLeft() {
//            return left;
//        }
//        public Node getRight() {
//            return right;
//        }
//        public int getValue() {
//            return value;
//        }
//        public void setLeft(Node left) {
//            this.left = left;
//        }
//        public void setRight(Node right) {
//            this.right = right;
//        }
//        public void setValue(int value) {
//            this.value = value;
//        }
//
//    }

    public Node root;
    public static final String IN_ORDER_TRAVERSE = "inOrderTraverse";
    public static final String PRE_ORDER_TRAVERSE = "preOrderTraverse";
    public static final String POST_ORDER_TRAVERSE = "postOrderTraverse";

    /**
     * 탐색 연산
     * 1. 왼쪽 자식 노드의 값은 현재 노드보다 항상 작아야 함.
     * 2. 오른쪽 자식 노드의 값은 현재 노드의 값 보다 항상 커야 함.
     */
    private boolean find(int value) {
        Node currentNode = root;   // 현재 위치한 노드
        while (currentNode != null) {
            if (currentNode.getValue() == value) {
                return true;
            } else if (currentNode.getValue() > value) {   // value : 한 노드 < currentNode : 어떤 노드 => 한 노드는 어떤 노드의 left
                currentNode = currentNode.getLeft();
            } else {   // 현재 위치한 노드의 값이 < 찾고자 하는 값보다 작으면
                currentNode = currentNode.getRight();    // 찾고자 하는 한 노도의 값은 < 어떤 노드의 왼쪽

            }
        }

        return false;
    }

    public boolean insert(int value) {
        Node newNode = new Node(value);   // 값을 받아 -> 새로운 newNode 생성
        if (find(value)) {   // find method 호출 -> value 가 있는지 Check -> 3번 전제조건 (3. 같은 키의 값을 갖는 노드는 존재하지 않음.) 확인
            return false;
        }
        if (root == null) {
            root = newNode;   // root == null -> newNode 를 => root 로 변경 후 return
            return true;
        }
        Node currentNode = root;
        Node parent;

        while(true) {
            parent = currentNode;   // root 노드의 부모는 root 노드 자신
            if (value < currentNode.getValue()) {   // 삽입하고자 하는 값인 value 가 currentNode(root)보다 작으면
                currentNode = currentNode.getLeft();   // 왼쪽 노드로 이동 -> 1번 전제조건 확인
                if(currentNode == null) {
                    parent.setLeft(newNode);
                    return true;
                }
            }else {
                currentNode = currentNode.getRight();
                if (currentNode == null) {
                    parent.setRight(newNode);
                    return true;
                }
            }
        }
    }

    public boolean delete(int value) {
        return false;
    }

    public List<Integer> traverse(Node focusNode, String orderType) {
        List<Integer> arr = new ArrayList<>();
        /**
         * reflection : 클래스의 구조를 분석하는 기능
         * -> Reflection 을 통한 동적 할당으로, 클래스를 -> Object 에 넣게 되면
         * -> Object 의 기본 함수만 사용하는 것이 아닌, 클래스의 구조 분석을 통해 메소드 검색/실행 가능
         */
        Method[] methods = BinaryTree.class.getDeclaredMethods();
        Method process = null;
        for (Method method : methods) {
            if(method.getName().equals(orderType)) {
                process = method;
            }
        }
        try {
            process.setAccessible(true);
            arr = (List<Integer>) process.invoke(new BinaryTree(), focusNode, arr);   // 실행하려고 하는 메소드의 대리자(delegate)를 실행

         // IllegalAccessException :  원인은 접근할수 없는 필드나 메소드에 접근
         // InvocationTargetException : 호출 된 메소드 또는 생성자에 의해 발생 된 예외를 랩핑
        } catch (IllegalAccessException | InvocationTargetException e) {
            e.printStackTrace();
        }
        return arr;
    }

    // TODO 전위 탐색 : root -> left -> right
    private List<Integer> preOrderTraverse(Node focusNode, List<Integer> arr) {
        if (focusNode != null) {
            arr.add(focusNode.getValue());
            inOrderTraverse(focusNode.getLeft(), arr);
            inOrderTraverse(focusNode.getRight(), arr);
        }

        return arr;
    }

    // TODO 중위 탐색 : left -> root -> right
    private List<Integer> inOrderTraverse(Node focusNode, List<Integer> arr) {
        if (focusNode != null) {
            inOrderTraverse(focusNode.getLeft(), arr);
            arr.add(focusNode.getValue());
            inOrderTraverse(focusNode.getRight(), arr);
        }

        return arr;
    }

    // TODO 후위 탐색 : left -> right -> root
    private List<Integer> postOrderTraverse(Node focusNode, List<Integer> arr) {
        if (focusNode != null) {
            inOrderTraverse(focusNode.getLeft(), arr);
            inOrderTraverse(focusNode.getRight(), arr);
            arr.add(focusNode.getValue());
        }

        return arr;
    }
    public List<Integer> bfs(Node focusNode) {
        if (focusNode == null) {
            return null;
        }
        List<Integer> result = new ArrayList<>();
        Queue<Node> queue = new LinkedList<>();

        queue.add(focusNode);
        while(!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Node poll = queue.poll();
                if (poll.getLeft() != null) {
                    queue.add(poll.getLeft());
                }
                if (poll.getRight() != null) {
                    queue.add(poll.getRight());
                }
                result.add(poll.getValue());
            }
        }
        return result;
    }

}
