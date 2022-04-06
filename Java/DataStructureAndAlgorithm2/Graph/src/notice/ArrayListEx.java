package notice;

import java.util.ArrayList;
import java.util.Iterator;

public class ArrayListEx {
    public static void main(String[] args) {
        ArrayList lst = new ArrayList();   // 타입 지정 X -> 기본형 : Object
        ArrayList<Integer> arr = new ArrayList<Integer>();

        // ArrayList 값 추가
        // ArrayList 는 값 추가/삭제 시 내부적으로 임시 배열을 생성해서 데이터를 복사하는 방법 사용
        // -> 빈번한 데이터 추가/삭제가 이루어질 때는 ArrayList << LinkedList 사용
        arr.add(3);
        arr.add(null);   // null 값도 add 가능
        arr.add(1, 10);   // index 1 뒤에 10 삽입

        // ArrayList 값 삭제
        /*
        arr.remove(1);   // index = 1 인 값 제거
        arr.clear();   // 모든 값 제거
         */

        // ArrayList 크기
        System.out.println("arr.size() : " + arr.size());

        // ArrayList 값 출력
        // 1) list 자체를 출력
        System.out.println("arr : " + arr);

        // 2) 특정 index 값 출력
        System.out.println("arr.get(1) : " + arr.get(1));

        // 3) for each 문으로 각각의 값에 접근하여 출력
        for (Integer x : arr) {
            System.out.print(x + " ");
        }
        System.out.println();

        // 4) Iterator 를 사용해서 값 출력
        Iterator<Integer> iter = arr.iterator();
        while(iter.hasNext()) {
            System.out.print(iter.next() + " ");
        }

    }
}
