package Round1.개미;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n;
    static ArrayList<Integer> pos, val, sortPos;

    public static int solution(ArrayList<Integer> pos, ArrayList<Integer> val) {
        HashMap<Integer, Integer> initMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            initMap.put(pos.get(i), val.get(i));
        }
        // initMap 을 value 기준 정렬 -> sortValMap
        List<Map.Entry<Integer, Integer>> sortValMap = new LinkedList<>(initMap.entrySet());
        sortValMap.sort(Map.Entry.comparingByValue());

        sortPos = new ArrayList<>();
        for(Map.Entry<Integer, Integer> entry : sortValMap){
            sortPos.add(entry.getKey());
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += Math.abs(pos.get(i) - sortPos.get(i));
        }

        return ans;
    }

    public static void main(String[] args) throws IOException {

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());

            for (int tc = 1; tc <= t; tc++) {

                st = new StringTokenizer(br.readLine());
                n = Integer.parseInt(st.nextToken());   // 개미 수
                pos = new ArrayList<>();
                val = new ArrayList<>();
                // 위치
                for (String stat : br.readLine().split(" ")) {
                    int num = Integer.parseInt(stat);
                    pos.add(num);
                }
                // 값
                for (String stat : br.readLine().split(" ")) {
                    int num = Integer.parseInt(stat);
                    val.add(num);
                }
                int ans = solution(pos, val);
                System.out.println(String.format("Case #%d", tc));
                System.out.println(ans);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
/*
3
5
1 2 4 5 6
9 2 1 1 2
5
1 2 7 8 10
7 3 3 3 7
5
4 5 6 7 10
9 10 10 10 9
 */