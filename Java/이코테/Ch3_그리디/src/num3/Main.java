package num3;

import java.util.Scanner;

// 곱하기 혹은 더하기
public class Main {
    public static int result, num;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String data = sc.next();

        result = data.charAt(0) - '0';
        for (int i = 0; i < data.length(); i++) {
            num = data.charAt(0) - '0';
            if (num <= 1 || result <= 1) result += num;
            else result *= num;
        }
        System.out.println(result);
    }
}
