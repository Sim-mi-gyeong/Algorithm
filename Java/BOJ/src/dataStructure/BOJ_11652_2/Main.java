package dataStructure.BOJ_11652_2;

import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static HashMap<Long, Integer> map;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        map = new HashMap<>();
        int maxVal = 1;   // n = 1 일 경우 -> INTEGER.MINVALUE 처리 불가
        for (int i = 0; i < n; i++) {
            long num = Long.parseLong(br.readLine());
            if (map.containsKey(num)) {
                int val = map.get(num);
                if (maxVal < val + 1) {
                    maxVal = val + 1;
                }
                map.replace(num, val + 1);
            } else {
                map.put(num, 1);
            }
        }
        List<Long> keyList = new ArrayList<>();
        for (Map.Entry<Long, Integer> entry : map.entrySet()){
            if (entry.getValue() == maxVal) {
                keyList.add(entry.getKey());
            }
        }
        Collections.sort(keyList);
        System.out.println(keyList.get(0));
    }
}
