package priorityQueue.ex1;

import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {

        /**
         * 우선순위 큐 선언
         */
        // TODO Integer 타입으로 우선순위 큐 선언(낮은 숫자 순으로 우선순위 결정) - MinHeap
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        // TODO Integer 타입으로 우선순위 큐 선언(높은 숫자 순으로 우선순위 결정) - MaxHeap
        PriorityQueue<Integer> pq2 = new PriorityQueue<>(Collections.reverseOrder());


        /**
         * 우선순위 큐에 값 추가 - 1 15 10 21 25 18 8 추가
         */
        int[] arr = {1, 15, 10, 21, 25, 18, 8};
        for (int i = 0; i < arr.length; i++) {
            pq.add(arr[i]);   // add() : Collection 클래스에서 가져오는 메서드 / offer() : Queue 클래스에서 가져오는 메서드
            pq2.add(arr[i]);
//            System.out.println(i+1 + " 번 항목이 추가될 때 마다 pq2 의 상태");
//            System.out.println("높은 숫자 순 우선순위 큐 : " + pq2);
        }
        // 낮은 숫자 순 우선순위 큐 출력
        System.out.println("낮은 숫자 순 우선순위 큐 : " + pq);
        // 높은 숫자 순 우선선위 큐 출력
        System.out.println("높은 숫자 순 우선순위 큐 : " + pq2);

        /**
         * 우선순위 큐에서 값 제거
         * poll(), remove() : 우선순위가 가장 높은 값 제거(poll() 은 우선순위가 가장 높은 값 리턴하고 삭제)
         * remove(int val) : 해당하는 값 제거 Ex) pq.remove(8) : 8 제거
         * clear() : 우선순위 큐의 모든 값 삭제
         * */

        pq.poll();
        System.out.println("우선순위가 가장 높은 값을 제거 한 후 : " + pq);

        pq.remove();
        pq.remove(15);
        System.out.println("우선순위가 가장 높은 값 + 15 제거 : " + pq);   // [8, 21, 10, 25]

        pq.clear();
        System.out.println("우선순위 큐 초기화 : " + pq);
    }
}
