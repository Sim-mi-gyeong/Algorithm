package cardSort;

import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        PriorityQueue<Integer> q = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            q.offer(sc.nextInt());
        }

        int sum = 0;
        while (q.size() > 1) {
            int tmp1 = q.poll();
            int tmp2 = q.poll();
            sum += (tmp1 + tmp2);   // 30 -> 30 + 60 -> 30 + 60 + 110
            q.offer(tmp1 + tmp2);
        }
        System.out.println(sum);
    }
}
