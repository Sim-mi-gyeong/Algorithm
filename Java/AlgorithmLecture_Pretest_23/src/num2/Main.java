package num2;

import java.io.*;
import java.util.StringTokenizer;

public class Main {

    static int n, m, k;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int maxVal = Integer.MIN_VALUE;

    public static int[][] copyMap(int[][] map) {
        int[][] tmp = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                tmp[i][j] = map[i][j];
            }
        }
        return tmp;
    }

    public static int getMaxCnt(int[][] map) {
        int tmpMaxVal = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                tmpMaxVal = Math.max(tmpMaxVal, map[i][j]);
            }
        }
        return tmpMaxVal;
    }

    public static void dfs(int cnt, int[][] map) {
        if (cnt == k) {
            maxVal = Math.max(maxVal, getMaxCnt(map));
            return;
        }

        int[][] tmpMap;
        for (int i = 0; i < 4; i++) {
            tmpMap = copyMap(map);
            if (i == 0) {
                for (int col = 0; col < m; col++) {
                    for (int row = 0; row < n; row++) {
                        if (tmpMap[row][col] != 0) {
                            if (row + 1 < 0 ||  row + 1 >= n) {
                                continue;
                            } else {
                                tmpMap[row + 1][col] += tmpMap[row][col];
                                tmpMap[row][col] = 0;
                                break;
                            }
                        }
                    }
                }
                dfs(cnt + 1, tmpMap);

            }
            else if (i == 1) {
                for (int row = 0; row < n; row++) {
                    for (int col = m - 1; col >= 0; col--) {
                        if (tmpMap[row][col] != 0) {
                            if (col - 1 < 0 ||  col - 1 >= m) {
                                continue;
                            } else {
                                tmpMap[row][col - 1] += tmpMap[row][col];
                                tmpMap[row][col] = 0;
                                break;
                            }
                        }
                    }
                }
                dfs(cnt + 1, tmpMap);
            }
            else if (i == 2) {
                for (int col = 0; col < m; col++) {
                    for (int row = n - 1; row >= 0; row--) {
                        if (tmpMap[row][col] != 0) {
                            if (row - 1 < 0 ||  row - 1 >= n) {
                                continue;
                            } else {
                                tmpMap[row - 1][col] += tmpMap[row][col];
                                tmpMap[row][col] = 0;
                                break;
                            }
                        }
                    }
                }
                dfs(cnt + 1, tmpMap);
            }
            else {
                for (int row = 0; row < n; row++) {
                    for (int col = 0; col < m; col++) {
                        if (tmpMap[row][col] != 0) {
                            if (col + 1 < 0 ||  col + 1 >= m) {
                                continue;
                            } else {
                                tmpMap[row][col + 1] += tmpMap[row][col];
                                tmpMap[row][col] = 0;
                                break;
                            }
                        }
                    }
                }
                dfs(cnt + 1, tmpMap);
            }
        }
    }

    public static int solve(int[][] map) {
        dfs(0, map);
        return maxVal;
    }

    public static void main(String[] args) throws IOException {

        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());

        for (int tc = 1; tc <= t; tc++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());

            int[][] map = new int[n][m];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < m; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int ans = solve(map);
            System.out.println(String.format("#%d %d", tc, ans));
        }
    }
}