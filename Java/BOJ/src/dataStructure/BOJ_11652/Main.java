package dataStructure.BOJ_11652;

import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static HashMap<Long, Integer> map;

    public static void main(String[] args) throws IOException {

        map = new HashMap<>();
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            long num = Long.parseLong(br.readLine());
            if (map.containsKey(num)) {
                map.replace(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }

        // HashMap 정렬 - Value 값 기준 정렬(오름차순 정렬)
        List<Map.Entry<Long, Integer>> entryList = new ArrayList<>(map.entrySet());
        Collections.sort(entryList, new Comparator<Map.Entry<Long, Integer>>() {
            @Override
            public int compare(Map.Entry<Long, Integer> o1, Map.Entry<Long, Integer> o2) {
                if (Integer.compare(o1.getValue(), o2.getValue()) == 0) {   // 카드 개수가 동일한 경우
                    return Long.compare(o1.getKey(), o2.getKey());   // 카드 숫자대로 오름차순 정렬
                }
                return (-1) * Integer.compare(o1.getValue(), o2.getValue());   // 카드 개수대로 내림차순 정렬
            }
        });

        for (Map.Entry<Long, Integer> entry : entryList) {
            System.out.println(entry.getKey());
            break;
        }
    }
}

/*
5
2
2
2
1
1

5
4611686018427387904
4611686018427387904
3
3
1
 */