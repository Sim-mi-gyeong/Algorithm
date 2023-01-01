package bruteForce.BOJ_17281;

import java.io.*;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int[][] inning;
    static boolean[] select; // 아래 순열에서 선수 선택 여부에 사용될 boolean 타입 배열
    static int[] seq;   // 각 선수별 타순
    static int maxScore;

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());

        inning = new int[n + 1][9];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());   // 한 줄 입력 받고
            for (int j = 0; j < 9; j++) {
                inning[i][j] = Integer.parseInt(st.nextToken());   // 띄어쓰기로 구분된 각 숫자 = 각 이닝에서 1번 ~ 9번 선수의 결과
            }
        }

        select = new boolean[9];
        seq = new int[9];

        select[3] = true;   // 1번 타자의 타순 = 4번 고정
        seq[3] = 1;

        maxScore = 0;
        perm(1);   // 2번 선수부터 ~ 9번 선수까지 가능한 순서 경우 구하기

        bw.write(maxScore + "\n");
        bw.flush();
        bw.close();
        br.close();

    }

    public static void perm(int num) {   // num 은 선수의 번호이자, 각 선수별로 순서를 할당한 횟수 -> 1번 선수를 제외하고 차례대로 선수의 순서 처리
        if (num == 9) {
            play();
            return;
        }

        for (int i = 0; i < 9; i++) {
            if (select[i]) {   // 이미 선택된 경우
                continue;
            }
            select[i] = true;
            seq[i] = num;
            perm(num + 1);
            select[i] = false;
        }
    }

    public static void play() {
        int tmpScore = 0;
        int thisPlayer = 0;   // 처음 시작하는 타자의 순서
        int base1, base2, base3;

        for (int i = 1; i <= n; i++) {   // n 번째 이닝까지
            int outCnt = 0;
            base1 = 0; base2 = 0; base3 = 0;

            while (outCnt < 3) {
                int hitResult = inning[i][seq[thisPlayer]];

                switch (hitResult) {
                    case 0:
                        outCnt++;
                        break;
                    case 1:   // 안타
                        tmpScore += (base3);
                        base1 = 1; base2 = base1; base3 = base2;
                        break;
                    case 2:   // 2루타
                        tmpScore += (base2 + base3);
                        base1 = 0; base2 = 1; base3 = base1;
                        break;
                    case 3:   // 3루타
                        tmpScore += (base1 + base2 + base3);
                        base1 = 0; base2 = 0; base3 = 1;
                        break;
                    case 4:   // 홈런
                        tmpScore += (1 + base1 + base2 + base3);
                        base1 = 0; base2 = 0; base3 = 0;
                        break;
                }

                thisPlayer = (thisPlayer + 1) % 9;

                if (outCnt == 3) {
                    break;
                }
            }

//            if (outCnt == 3) {
//                break;
//            }

            // thisPlayer 1로 초기화해 주는 이유
            // 1~9번까지 타자가 한 이닝에 전부 안타를 쳐서 아웃카운트가 발생하지 않게 되면,
            // 위 반복문이 무한 루프를 돌기때문에 thisPlayer = 1로 초기화해야 함.
            thisPlayer = 0;
        }

        maxScore = Math.max(maxScore, tmpScore);

    }
}
