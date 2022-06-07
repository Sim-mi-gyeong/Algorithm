package fractionalKnapsack;

import java.util.Scanner;

public class FractionalKnapsack {

    int n;   // 물건들의 개수
    double weight[];   // 각 물건들의 무게
    double value[];   // 각 물건의 가치
    double W;   // 배낭의 용량
    double[] unitValue;   // 단위 무게당 가치

    // 물건의 수, 각 물건의 무게, 각 물건의 가치와 배낭의 용량 입력 받기
    public void inputData() {

        Scanner sc = new Scanner(System.in);

        System.out.print("물건들의 수를 입력하세요. ");
        n = sc.nextInt();

        weight = new double[n];
        value = new double[n];

        System.out.print("각 물건의 무게를 입력하세요. ");
        for (int i = 0; i < n; i++) {
            weight[i] = sc.nextDouble();
        }

        System.out.print("각 물건의 가치를 입력하세요. ");
        for (int i = 0; i < n; i++) {
            value[i] = sc.nextDouble();
        }

        System.out.print("배낭의 용량을 입력하세요. ");
        W = sc.nextDouble();

        sc.close();
    }

    // 배낭에 다음으로 넣을 물건의 인덱스 찾기
    public int getNextItem() {
        double highest = 0;
        int index = -1;

        // 남아 있는 물건들 중 단위 무게 당 가치가 가장 높은 물건의 인덱스 찾기
        for (int i = 0; i < value.length; i++) {
            if (unitValue[i] > highest) {
                highest = unitValue[i];
                index = i;
            }
        }

        return index;
    }

    public void fractionalKnapsack() {
        unitValue = new double[n];   // 단위 무게당 가치
        int item;

        // 각 물건의 단위 무게 당 가치 계산
        for (int i = 0; i < n; i++) {
            unitValue[i] = value[i] / weight[i];
        }
        System.out.println();

        double cW = 0;   // 배낭에 담길 물건들의 무게의 합을 0으로 초기화
        double cV = 0;   // 배낭에 담긴 물건들의 가치의 합을 0으로 초기화

        // 단위 무게 당 가치가 가장 큰 물건 찾기
        item = getNextItem();

        // 배낭에 채울 물건들이 남아있고, 배낭이 채워지지 않은 동안 반복
        while ((item != -1 && cW + weight[item] <= W)) {
            // 배낭에 물건 item 의 전부를 넣는다
            cW += weight[item];
            cV += value[item];
            System.out.println("물건 " + (item + 1) + " 의 " + weight[item] + " 을 배낭에 넣는다.");

            // 물건 item 을 다음으로 배낭에 넣을 물건들의 목록에서 제거
            unitValue[item] = 0;
            // 남아있는 물건들 중에서 단위 무게당 가치가 가장 큰 물건 찾기
            item = getNextItem();
        }

        // 배낭의 용량이 남아 있으면 배낭에 물건 item 의 일부를 넣는다
        if (W - cW > 0) {
            System.out.println("물건 " + (item + 1) + " 의 " + (W - cW) + " 을 배낭에 넣는다.");

            cV += unitValue[item] * (W-cW);
            cW += (W - cW);

            System.out.println("\n 총 가치 = " + cV + " , 총 무게 = " + cW);
        }
    }

    public static void main(String[] args) {

        FractionalKnapsack fks = new FractionalKnapsack();

        // 물건들의 수, 각 물건의 무게, 각 물건의 가치와 베낭의 용량을 입력받기
        fks.inputData();

        // 배낭에 담긴 물건들, 물건들의 무게 합과 가치의 합 계산
        fks.fractionalKnapsack();
    }
}
