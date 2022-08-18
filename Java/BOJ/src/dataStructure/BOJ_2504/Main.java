package dataStructure.BOJ_2504;

import java.io.*;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char[] arr = br.readLine().toCharArray();

        int tmp = 1;
        int ans = 0;
        Stack<Character> stack = new Stack<>();

        boolean flag = true;

        // 짝이 맞는 경우에 tmp 에 곱을 하는 것이 아닌, push 할 떄 곱을 하고 -> 짝이 완성되면 결과값에 반영 : 괄호가 포함된 경우 처리 가능
        for(int i = 0; i < arr.length; i++) {
            char c = arr[i];
            if (c == '(') {
                stack.push(c);
                tmp *= 2;
            }
            if (c == '[') {
                stack.push(c);
                tmp *= 3;
            }
            else if (c == ')') {
                // 예외, 오류 상황 먼저 처리하기 - 스택이 null 인 경우
                if (stack.isEmpty() || stack.peek() != '(') {
                    flag = false;
                    break;
                }
                if (arr[i-1] == '(') {
                    ans += tmp;
                }
                stack.pop();
                tmp /= 2;

            }
            else if (c == ']') {
                if (stack.isEmpty() || stack.peek() != '[') {
                    flag = false;
                    break;
                }
                if (arr[i-1] == '[') {
                    ans += tmp;
                }
                stack.pop();
                tmp /= 3;
            }
        }
        if (!flag || !stack.isEmpty()) {
            bw.write(0 + "\n");
        } else {
            bw.write(ans + "\n");
        }
        bw.flush();
        bw.close();
    }
}