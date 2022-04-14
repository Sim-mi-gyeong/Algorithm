# 파이썬의 장점을 살린 방식

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]  # 피벗을 제외한 리스트

    # 피벗보다 작은 경우 -> 왼쪽 리스트에 담기
    leftSide = [x for x in tail if x <= pivot]
    # 피벗보다 큰 경우 -> 오른쪽 리스트에 담기
    rightSide = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽/오른쪽 부분에서 각각 정렬 수행 -> 전체 리스트 반환
    return quickSort(leftSide) + [pivot] + quickSort(rightSide)


print(quickSort(array))
