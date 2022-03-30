package adjacencyList;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int v = sc.nextInt();   // 정점의 개수
        int e = sc.nextInt();   // 간선의 개수

        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        // 리스트 인덱스를 1 ~ 로 하기 위해 dummy data 로 우선 삽입
        arr.add(new<Integer> ArrayList());
        for (int i = 0; i < v; i++) {
            arr.add(new<Integer> ArrayList());
        }
        for (int i = 0; i < e; i++) {
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();
        }
        // 인접 리스트 출력
        for (int i = 1; i <= v; i++) {
            Iterator<Integer> iter = arr.get(i).iterator();
            System.out.print("[ " + i + " ]");
            while (iter.hasNext()) {
                System.out.print(iter.next() + " ");
            }
            System.out.println();
        }
    }
}