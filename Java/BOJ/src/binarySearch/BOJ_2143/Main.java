package binarySearch.BOJ_2143;
// 두 배열의 합
import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int t, n, m;
    static int[] a, b;

    public static void main(String[] args) throws IOException {
        t = Integer.parseInt(br.readLine());
        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        m = Integer.parseInt(br.readLine());
        b = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        int aSize = n * (n+1) / 2;
        int bSize = m * (m+1) / 2;
        long[] aSumArr = new long[aSize];
        long[] bSumArr = new long[bSize];

        int idx = 0;
        for (int i = 0; i < n; i++) {
            int tmp = 0;
            for (int j = i; j < n; j++) {
                tmp += a[j];
                aSumArr[idx++] = tmp;
            }
        }

        idx = 0;
        for (int i = 0; i < m; i++) {
            int tmp = 0;
            for (int j = i; j < m; j++) {
                tmp += b[j];
                bSumArr[idx++] = tmp;
            }
        }

        Arrays.sort(aSumArr);
        Arrays.sort(bSumArr);

        long ans = 0;
        for (int i = 0; i < aSize;) {
            long aTmp = aSumArr[i];
            long aCnt = upperBound(aSumArr, aTmp) - lowerBound(aSumArr, aTmp);
            long bCnt = upperBound(bSumArr, t - aTmp) - lowerBound(bSumArr, t - aTmp);

            ans += (aCnt * bCnt);
            i += aCnt;
        }
        bw.write(ans + "\n");
        bw.flush();
        bw.close();
    }

    public static long upperBound(long[] arr, long t) {
        int left = 0;
        int right = arr.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (t >= arr[mid]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return right;
    }

    public static long lowerBound(long[] arr, long t) {
        int left = 0;
        int right = arr.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (t <= arr[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return right;
    }
}