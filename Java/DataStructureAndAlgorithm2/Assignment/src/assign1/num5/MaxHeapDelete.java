package assign1.num5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class MaxHeapDelete {
    private static ArrayList<Integer> heap;
    private static int target;

    public MaxHeapDelete() {
        heap = new ArrayList<Integer>();
        heap.add(0);
    }

    //TODO 삽입 메서드
    public void insert(int val) {
        //TODO 가장 마지막 위치에 입력받은 값 삽입
        heap.add(val);

        int p = heap.size()-1;
        //TODO 루트까지 이동 -> 자식이 더 크면 교환
        while(p>1 && heap.get(p)> heap.get(p/2)) {
            int tmp = heap.get(p/2);
            heap.set(p/2, heap.get(p));
            heap.set(p, tmp);

            p /= 2;
        }
    }

    //TODO 삭제 메서드
    public static int delete() {
        // 힙이 비어있는 경우 -> return 0
        if(heap.size()-1 < 1) {
            return 0;
        }

        //TODO 삭제할 루트 노드 값 저장
        int targetIdx = heap.indexOf(target);
        int deleteItem = heap.get(targetIdx);

        //TODO 가장 마지막 자식 노드 위치에 넣고 마지막 값 삭제
        heap.set(targetIdx, heap.get(heap.size()-1));
        heap.remove(heap.size()-1);

        int pos = 1;   // 루트에 새로 넣은 노드의 인덱스 정보
        while((pos*2)<heap.size()) {

            int max = heap.get(pos*2);
            int maxPos = pos*2;

            if ((pos * 2 + 1) < heap.size() && max < heap.get(pos * 2 + 1)) {
                max = heap.get(pos * 2 + 1);
                maxPos = pos * 2 + 1;
            }

            // TODO 부모 노드의 값이 더 큰 경우 반복문 탈출
            if(heap.get(pos) > max){
                break;
            }

            // TODO 자식 노드의 값이 더 큰 경우 교환
            int tmp = heap.get(pos);
            heap.set(pos, max);
            heap.set(maxPos, tmp);
            pos = maxPos;
        }

        for (int i = 1; i < heap.size(); i++) {
            System.out.print(heap.get(i) + " ");
        }
        System.out.println();

        return deleteItem;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("힙 노드 개수 입력 ");
        int n = Integer.parseInt(br.readLine());

        MaxHeapDelete heap = new MaxHeapDelete();

        System.out.println("힙 노드 정보 입력");
        for (int i = 0; i < n; i++) {
            int value = Integer.parseInt(br.readLine());

            if (value == 0) {
                System.out.println(heap.delete());
            } else {
                heap.insert(value);
            }
        }

        System.out.print("삭제할 노드 : ");
        target = Integer.parseInt(br.readLine());

        System.out.println("------------------");
        System.out.println("힙 삭제 수행");
        System.out.print("남은 heap 의 노드 정보 출력 : ");

        System.out.println("삭제된 노드 : " + heap.delete());
    }
}

/*
6
20
15
17
5
7
13
 */
