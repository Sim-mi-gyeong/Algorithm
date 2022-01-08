# List Comprihension을 사용한 퀵 정렬

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면, 종료
    if len(array) <= 1: return array
    pivot = array[0]   # 피벗은 첫 번째 원소
    tail = array[1:]   # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]   # 분할된 왼쪽 부분
    # 피벗을 제외한 리스트에서 원소를 하나씩 확인하며 Pivot 보다 큰 값들만 오른쪽 위치에 넣음
    right_side = [x for x in tail if x > pivot]   # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
    # 왼쪽 부분에 대해 퀵 정렬을 수행한 결과 리스트 + 현재 Pivot 값을 담고 있는 리스트 + 오른쪽 부분에 대해 퀵 정렬을 수행한 결과 리스트
    return quick_sort(left_side) + pivot + quick_sort(right_side)

print(quick_sort(array))
    