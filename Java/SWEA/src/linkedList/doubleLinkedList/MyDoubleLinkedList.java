package linkedList.doubleLinkedList;

import java.util.List;

public class MyDoubleLinkedList<E> {

    private Node<E> head;   // 노드의 첫 부분
    private Node<E> tail;   // 노드의 마지막 부분
    private int size;   // 요소 개수

    public MyDoubleLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    /**
     * 특정 위치의 노드를 반환하는 메서드
     */
    private Node<E> search(int index) {

        // 범위 밖(잘못된 위치)일 경우 예외 처리
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }

        // index 가 size(마지막)에 가까울 경우 뒤에서부터 탐색 - 역방향 탐색
        if (index + 1 > size / 2) {   // (size / 2) > index
            Node<E> x = tail;
            for (int i = size - 1; i > index; i--) {
                x = x.prev;
            }
            return x;
        }
        // index 가 0(처음)에 가까울 경우 앞에서부터 탐색 - 순차 탐
        else {
            Node<E> x = head;
            for (int i = 0; i < index; i++) {
                x = x.next;
            }
            return x;
        }
    }

    public void addFirst(E value) {
        Node<E> newNode=  new Node<E>(value);   // 새 노드 생성
        newNode.next = head;   // 새 노드의 다음 노드로 head 노드를 연결

        /**
         * head 가 null 이 아닌 경우에만 기존 head 노드의 prev 변수가 -> 새 노드를 가리키도록 한다
         * 이유는, 기존 head 노드가 없는 경우 (= null)
         * -> 데이터가 아무것도 없던 상태 -> head.prev 를 하면 잘못 참조가 된다.
        */
        if (head != null) {
            head.prev = newNode;
        }
        head = newNode;
        size++;

        /**
         * 새로 추가하는 노드가 다음으로 가리킬 노드가 없는 경우 (= 데이터가 새 노드밖에 없는 경우)
         * - 데ㅇ터가 한 개 (새로운 노드) 밖에 없으므로, 새 노드는 처음 노드이자 마지막 노드
         * -> tail = head
         */
        if (head.next == null) {
            tail = head;
        }
    }

    public boolean add(E value) {
        addLast(value);
        return true;
    }

    public void addLast(E value) {
        Node<E> newNode = new Node<E>(value);

        if (size == 0) {
            addFirst(value);
            return;
        }

        // 새 노드를 넣기 전, 리스트에 하나라도 데이터가 있는 경우
        tail.next = newNode;
        newNode.prev = tail;
        tail = newNode;
        size++;
    }

    public E get(int index) {
        return search(index).data;
    }
}

/**
 * 가장 기본적색 데이터를 담을 Node 클래스
 * @param <E>
 */
class Node<E> {
    E data;
    Node<E> prev;   // 이전 노드 객체를 가리키는 레퍼런스 변수
    Node<E> next;   // 다음 노드 객체를 가리키는 레퍼런스 노드

    Node(E data) {
        this.data = data;
        this.prev = null;
        this.next = null;
    }
}
