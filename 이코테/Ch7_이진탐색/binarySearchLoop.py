# 이진 탐색(반복문)
def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        # 현재 확인하는 값이 > 목효 값보다 큰 경우, 즉 arr[mid]의 왼쪽을 탐색해야 하는 경우
        elif arr[mid] > target:   
            end = mid - 1
        # 현재 확인하는 값이 < 목표 값보다 작은 경우, 즉 arr[mid]의 오른쪽을 탐색해야 하는 경우
        else:
            start = mid + 1

    return None    # 반복문을 돌 동안찾지 못한 경우

n, target = map(int, input().split())
arr = list(map(int, input().split()))
result = binarySearch(arr, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)