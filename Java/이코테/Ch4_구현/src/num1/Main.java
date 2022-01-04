package num1;

import java.util.ArrayList;
import java.util.Scanner;

// 문자열 재정렬
// 문자열 입력 시 문자를 하나씩 확인
// -> 숫자인 경우 따로 합 계산
// -> 알파벳은 별도의 리스트에 저장
// 리스트에 저장된 알파벳을 정렬해 출력 + 합계를 뒤에 붙여 출력
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String data = sc.nextLine();
        ArrayList<Character> str = new ArrayList<Character>();
        int sum = 0;

        for (int i = 0; i < data.length(); i++) {
            char c = data.charAt(i);
//            if(c >= '0' && c <= '9') sum += (c - '0');
            if(!Character.isAlphabetic(c)) sum += (c - '0');
            else str.add(c);
        }

//        if(sum!=0) {
////            for (Character x: str) System.out.print(x + " ");
//            for (int i = 0; i < str.size(); i++) {
//                System.out.print(str.get(i) + "");
//            }
//            System.out.print(sum);
//        }
//        else {
//            for (int i = 0; i < str.size(); i++) {
//                System.out.print(str.get(i) + "");
//            }
//        }
        for (int i = 0; i < str.size(); i++) {
            System.out.print(str.get(i) + "");
        }
        if (sum != 0) System.out.print(sum);

    }
}
