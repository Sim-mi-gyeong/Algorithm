package adjacencyList;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class UnDirectedGraphArrayList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int v = sc.nextInt();
        int e = sc.nextInt();

        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        arr.add(new ArrayList<>());
        for (int i = 0; i < v; i++) {
//            arr.add(new<Integer> ArrayList());
            arr.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < e; i++) {
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();

            arr.get(v1).add(v2);
            arr.get(v2).add(v1);
        }

        // 인접리스트 출력
        for (int i = 1; i <= v; i++) {
            Iterator<Integer> iter = arr.get(i).iterator();
            System.out.print("[ " + i + " ] : ");
            while(iter.hasNext()) {
                System.out.print(iter.next() + " ");
            }
            System.out.println();
        }
    }
}
/*
6 8
1 2
1 3
2 3
2 4
3 4
3 5
4 5
4 6
 */