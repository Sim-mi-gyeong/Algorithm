# x의 '첫 번째' 위치 구하기
def binarySearchStart(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            # target == mid -> mid가 target의 첫 번째 위치일 때
            if mid - 1 < 0 or arr[mid - 1] != target:   
                return mid
            # target == mid -> mid가 target의 첫 번째가 아닐 때 -> 범위를 줄여 mid 왼쪽 부분 탐색
            else:
                end = mid - 1
        # target 이 mid 의 완쪽에 있을 때 -> 범위 줄여 mid 왼쪽 탐색
        elif arr[mid] >= target:
            end = mid - 1
        # target 이 mid 의 오른쪽에 있을 때 -> 범위 줄여 mid 오른쪽 탐색
        else:
            start = mid + 1   
    
    return -1   # 찾는 값이 배열에 존재하지 않는 경우

# x의 '마지막' 위치 구하기
def binarySearchEnd(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            # target == mid -> mid 가 target의 마지막 위치일 때
            if mid + 1 >= len(arr) or arr[mid + 1] != target:
                return mid
            # target == mid -> mid 가 target의 마지막 위치가 아닐 떼 -> 범위 줄여 mid의 오른쪽 부분 탐색    
            else:
                start = mid + 1
        elif arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return -1

n, x = map(int, input().split())
arr = list(map(int, input().split()))

startLoc = binarySearchStart(arr, x, 0, len(arr) - 1)
endLoc = binarySearchEnd(arr, x, 0, len(arr) - 1)
cnt = endLoc - startLoc + 1

if startLoc == -1: print(-1)
else: print(cnt)

'''
[입력 예시]
7 2
1 1 2 2 2 2 3
[출력 예시]
4
'''

# [다른 풀이]
# 이진 탐색으로 x 가 있는지 확인하고 -> x가 있다면, x 위치에서 앞으로/뒤로 x 개수 세기
# -> x의 개수가 많지 않다면 시간 복잡도 O(logN) 가능
# if) N개의 원소를 가지고 있는 수열이 x로만 이루어진 경우 -> O(N)