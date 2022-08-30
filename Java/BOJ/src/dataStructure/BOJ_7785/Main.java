package dataStructure.BOJ_7785;
// 회사에 있는 사람
import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static HashMap<String, String> map;

    public static void main(String[] args) throws IOException {

        map = new HashMap<>();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String memo = st.nextToken();

            if (!map.containsKey(name)) {
                map.put(name, memo);
            } else {
                map.remove(name);
            }
        }

        List<Map.Entry<String, String>> entryList = new ArrayList<>(map.entrySet());
        Collections.sort(entryList, new Comparator<Map.Entry<String, String>>() {

            @Override
            public int compare(Map.Entry<String, String> o1, Map.Entry<String, String> o2) {
                return o2.getKey().compareTo(o1.getKey());
            }
        });

        for (Map.Entry<String, String> entry : entryList) {
            bw.write(entry.getKey() + "\n");
        }
        bw.flush();
        bw.close();
    }
}
