package assign1.num7;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class AdjacencyList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int v = sc.nextInt();
        int e = sc.nextInt();
        ArrayList<ArrayList<Integer>> adList = new ArrayList<>();
        adList.add(new ArrayList<Integer>());

        for (int i = 0; i < v; i++) {
            adList.add(new ArrayList<Integer>());
        }

        // TODO 인접 노드 추가
        for (int i = 0; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            adList.get(a).add(b);
        }

        // TODO 인접 리스트 출력
        for (int i = 1; i <= v; i++) {
            Iterator<Integer> iter = adList.get(i).iterator();
            System.out.print("[ " + i + " ] : ");
            while(iter.hasNext()) {
                System.out.print(iter.next() + " ");
            }
            System.out.println();
        }
    }
}

/*
5 7
1 2
1 3
1 4
2 4
2 5
3 4
4 5
 */

