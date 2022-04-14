array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):  # 전체 데이터 영역에서 시작 -> 가장 작은 데이터와 위치가 바뀔 인덱스
    minIdx = i  # 정렬되지 않은 원소들 중 가장 앞쪽의 원소 -> 가장 작은 원소의 인덱스로 설정하고,
    for j in range(i + 1, len(array)):  # 정렬되지 않은 원소들 중 가장 작은 원소(minIdx 보다 작은) 찾기
        if array[minIdx] > array[j]:
            minIdx = j
    array[i], array[minIdx] = array[minIdx], array[i]
print(array)
