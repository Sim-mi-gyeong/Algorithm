package Num3;
// MBTI

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static int num, n;   // mbti 종류 수, 각 문자 포함 개수
    static long minCost, ans;
    static String[] mbtiArr;
    static Character[] alphaArr;
    static boolean[] visited;
    static HashMap<String, Integer> map;
    static HashMap<Character, Integer> alphaMap;

    public static long combination(String[] arr, boolean[] visited, int start, int n, int r, HashMap<String, Integer> map) {
        if(r == 0) {
            long tmpCost = 0;
            boolean tmpCheck = true;
            // 해당 조합에서 비용 및 각 문자 계산
            for (int i = 0; i < arr.length; i ++) {
                tmpCost += map.get(arr[i]);
                // 각 단어가 개수를 충족하는지
                for (int j = 0; j < 4; j++) {
                    alphaMap.put(arr[i].charAt(j), alphaMap.get(arr[i].charAt(j)) + 1);
                }
            }
            for (Map.Entry<Character, Integer> entry : alphaMap.entrySet()) {
                if (entry.getValue() >= num) {
                    continue;
                } else {
                    tmpCheck = false;
                }
            }

            if (tmpCheck) {
                minCost = Math.min(minCost, tmpCost);
            }

        }

        for(int i = start; i < n; i++) {
            visited[i] = true;
            combination(arr, visited, i + 1, n, r - 1, map);
            visited[i] = false;
        }

        return minCost;
    }

    // 배열 출력
    static void print(String[] arr, boolean[] visited, int n) {
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
    }

    public static long solution(HashMap<String, Integer> map) {
        return 0;
    }

    public static void main(String[] args) throws IOException {

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());

            for (int tc = 1; tc <= t; tc++) {

                mbtiArr = new String[]{"ENFJ", "ENFP", "ENTJ", "ENTP", "ESFJ", "ESFP", "ESTJ", "ESTP", "INFJ", "INFP", "INTJ", "INTP", "ISFJ", "ISFP", "ISTJ", "ISTP"};
                alphaArr = new Character[]{'E', 'S', 'T', 'J', 'I', 'N', 'F', 'P'};
                num = mbtiArr.length;
                visited = new boolean[num];
                for (int i = 0; i < num; i++) {
                    ans = combination(mbtiArr, visited, 0, 16, i, map);
                }
                map = new HashMap<>();
                alphaMap = new HashMap<Character, Integer>();
                for (int i = 0; i < alphaArr.length; i++) {
                    if (!alphaMap.containsKey(alphaArr[i])) {
                        alphaMap.put(alphaArr[i], 0);
                    }
                }
                st = new StringTokenizer(br.readLine());
                n = Integer.parseInt(st.nextToken());
                String[] str = br.readLine().split(" ");
                for (int i = 1; i <= num; i++) {
                    int cost = Integer.parseInt(str[i-1]);
                    map.put(mbtiArr[i-1], cost);
                }

                System.out.println(String.format("#%d %d", tc, ans));

            }

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
