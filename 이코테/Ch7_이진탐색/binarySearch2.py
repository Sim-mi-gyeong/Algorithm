# 이진 탐색(재귀 함수)
def binarySearch(arr, target, start, end):
    if start > end: 
        return None
    mid = (start + end) // 2
    # 찾고자 하는 값을 찾은 경우 -> 중간점 인덱스 반환
    if arr[mid] == target:
        return mid
    # 중간점 값보다 > 찾고자 하는 값 -> 왼쪽 확인
    elif arr[mid] > target:
        return binarySearch(arr, target, start, mid - 1) 
    # 중간점 값보다 < 찾고자 하는 값 -> 오른쪽 확인
    else:
        return binarySearch(arr, target, mid + 1, end)

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binarySearch(arr, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.') 
else:
    print(result + 1)   # 결과 : index + 1

'''
[입력 예시]
10 7
1 3 5 7 9 11 13 15 17 19
[출력 예시]
4

[입력 예시]
10 7
1 3 5 6 9 11 13 15 17 19
[출력 예시]
원소가 존재하지 않습니다.
'''