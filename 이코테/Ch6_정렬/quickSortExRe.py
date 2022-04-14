array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quickSort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:  # 엇갈릴 때까지 반복 - left가 가리키는 인덱스 > right가 가리키는 인덱스 -> 탈출
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈린 이후 -> right 이 가리키는 원소가 더 작은 값 -> 작은 값과 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면, 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽(pivot 보다 작은 값) / 오른쪽(pivot 보다 큰 값) 부분 각각 정렬 수행
    quickSort(array, start, right - 1)
    quickSort(array, right + 1, end)


quickSort(array, 0, len(array) - 1)
print(array)
