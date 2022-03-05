package intervalSum;

public class Main {
    public static int n = 5;
    public static int[] arr = {10, 20, 30, 40, 50};
    public static int[] prefixSum = new int[n+1];

    public static void main(String[] args) {
        int sumValue = 0;

        for (int i = 0; i < n; i++) {
            sumValue += arr[i];
            prefixSum[i+1] = sumValue;
        }
        int left = 3;
        int right = 4;
        System.out.println(prefixSum[right] - prefixSum[left - 1]);
    }
}
