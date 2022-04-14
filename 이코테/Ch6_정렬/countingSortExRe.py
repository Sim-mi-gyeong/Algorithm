array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):  # 안쪽 반복문 전체 수행 횟수 n -> 결과적으로 이중반복문의 시간복잡도 = O(N + K)
        print(i, end=" ")

# 공간복잡도 O(N+K) : 정렬을 수행할 데이터 개수 N, 데이터 중 가장 큰 값의 크기, K 만큼의 공간 필요
