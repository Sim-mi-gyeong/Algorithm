package example;

import java.util.LinkedList;
import java.util.Queue;

public class QueueEx {
    public static void main(String[] args) {
//        Queue q = new LinkedList();
        Queue<Integer> q = new LinkedList<>();

        q.offer(5);
        q.offer(2);
        q.offer(3);
        q.offer(7);
        q.poll();   // 대기열에 쌓여있는 원소 중 하나를 꺼내 확인 -> 꺼내진 원소를 바로 반환
        q.offer(1);
        q.offer(4);
        q.poll();

        while(!q.isEmpty()) {
            System.out.print(q.poll() + " ");
        }

    }
}
