package Round1.개미_제출용;

import java.util.*;

class Solution {

    static int Answer;
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

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int test_case = 0; test_case < T; test_case++) {

			n = sc.nextInt();
            pos = new ArrayList<>();
            val = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                pos.add(sc.nextInt());
            }
            for (int i = 0; i < n; i++) {
                val.add(sc.nextInt());
            }

            Answer = solution(pos, val);
            // Print the answer to standard output(screen).
            System.out.println("Case #"+(test_case+1));
            System.out.println(Answer);
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