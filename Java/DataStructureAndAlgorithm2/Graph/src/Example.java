import java.util.Iterator;
import java.util.LinkedList;

public class Example {
    public static void main(String[] args) {
        LinkedList<Integer> arr = new LinkedList<>();

        arr.addFirst(1);
        arr.addLast(2);
        arr.add(3);
        arr.add(1, 10);

        // LinkedList 크기
        System.out.println("arr.size() : " + arr.size());

        // list 전체 출력
        System.out.println(arr);
        // for each 구문으로 arr 에 있는 값들을 하나하나 출력
        for(Integer x : arr) {
            System.out.print(x + " ");
        }
        System.out.println();
        // Iterator 를 통해 list 를 iterator 로 줄 세워 -> 줄을 뽑아 출력
        Iterator<Integer> iter = arr.iterator();
        while(iter.hasNext()) {
            System.out.print(iter.next() + " ");
        }

        // LinkedList 값 검색
        System.out.println("arr.contains(1) : " + arr.contains(1));
        System.out.println("arr.indexOf(1) : "+ arr.indexOf(1));
    }
}
