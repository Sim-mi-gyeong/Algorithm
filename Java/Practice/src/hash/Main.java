package hash;

import javax.lang.model.type.IntersectionType;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        /**
         * HashMap 객체 선언 - (key,value) 형태
         * 1. put(key, value) : 데이터 추가
         * 2. remove(key) : 특정 데이터 삭제
         * 3. replace(key, 수정할 value) : 특정 데이터 수정
         * 4. get(key) : 특정 key 값에 따른 value 출력
         * 5. entrySet : 전체 목록에서 각각 key, value 출력
         */

        // TODO HashMap 선언
        HashMap<Integer, String> map = new HashMap<Integer, String>();

        // TODO HashMap 값 추가
        map.put(1, "monkey");
        map.put(2, "tiger");
        map.put(3, "giraffe");

        // TODO HashMap 값 삭제
        map.remove(2);
        // map.clear()   // 모든 값 제거

        // TODO HashMap 값 출력 - entrySet() 사용
        System.out.println(map);   // 전체 출력
        System.out.println(map.get(1));   // key = 1 의 value 값 얻기

        for (Map.Entry<Integer, String> entry : map.entrySet()) {
            System.out.println("key : " + entry.getKey() + "  value : " + entry.getValue());
        }

        System.out.println();

        // TODO HashMap 값 출력 - Iterator 사용
        Iterator<Map.Entry<Integer, String>> entries = map.entrySet().iterator();
        while (entries.hasNext()) {
            Map.Entry<Integer, String> entry = entries.next();
            System.out.println("key : " + entry.getKey() + "  value : " + entry.getValue());
        }
        System.out.println();

        System.out.println("값 추가 후 정렬");
        map.put(2, "rabbit");
        map.put(5, "deer");
        map.put(4, "bear");

        // TODO HashMap 키(key) 기준 정렬
        Object[] mapKey = map.keySet().toArray();
        Arrays.sort(mapKey);

        System.out.println("key 기준 오름차순 정렬 - Comparator 사용");
        for (Map.Entry<Integer, String> entry : map.entrySet()) {
            System.out.println("key : " + entry.getKey() + "  value : " + entry.getValue());
        }

        System.out.println();

        // TODO HashMap 값(value) 기준 정렬
        // Map.Entry 리스트
        List<Map.Entry<Integer, String>> entryList = new ArrayList<Map.Entry<Integer, String>>(map.entrySet());

        // Comparator 를 사용하여 정렬
        Collections.sort(entryList, new Comparator<Map.Entry<Integer, String>>() {
            // 값 비교
            public int compare(Map.Entry<Integer, String> obj1, Map.Entry<Integer, String> obj2) {
                // 오름차순 정렬
                return obj1.getValue().compareTo(obj2.getValue());
                // 내림차순 정렬
//                return obj2.getValue().compareTo(obj1.getValue());
            }
        });
        // 결과 출력
        System.out.println("value 기준 오름차순 정렬 - Comparator 사용");
        for (Map.Entry<Integer, String> entry : entryList) {
            System.out.println("key : " + entry.getKey() + "  value : " + entry.getValue());
        }
        System.out.println();

        // TODO HashMap 키(key) 기준 정렬 - Comparator 사용
        HashMap<String, Integer> map2 = new HashMap<String, Integer>();

        map2.put("monkey", 1);
        map2.put("panda", 2);
        map2.put("deer", 3);
        map2.put("cat", 4);
        map2.put("dog", 5);

        List<Map.Entry<String, Integer>> list= new ArrayList<Map.Entry<String, Integer>>(map2.entrySet());

        Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {
            public int compare(Map.Entry<String, Integer> obj1, Map.Entry<String, Integer> obj2) {
                // 오름차순 정렬
                return obj1.getKey().compareTo(obj2.getKey());
                // 내림차순 정렬
//                return obj2.getKey().compareTo(obj1.getKey());
            }
        });

        System.out.println("key 기준 오름차순 정렬 - Comparator 사용");
        for (Map.Entry<String, Integer> entry: list) {
            System.out.println("key : " + entry.getKey() + "  value : " + entry.getValue());
        }




    }

}
