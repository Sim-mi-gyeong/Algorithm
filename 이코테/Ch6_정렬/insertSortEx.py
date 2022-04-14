# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 삽입하고자 하는 원소의 인덱스 - 인덱스 i부터 1까지 1씩 감소하며 반복
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동 (카드가 들어갈 곳은 각 카드의 왼쪽 부분)
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)
