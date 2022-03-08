n, m = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = max(arr)

while (start <= end):
    tmpSum = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            tmpSum += (i-mid)
    # 잘린 결과가 < 필요한 길이 보다 작은 경우 -> 중간점의 왼쪽 부분으로 이진탐색 수행
    if tmpSum < m:
        end = mid - 1
    # 잘린 결과가 > 필요한 길이 보다 큰 경우 -> 중간점의 오른쪽 부분으로 이진탐색 수행
    else:
        # 결과 저장하고,
        result = mid
        start = mid + 1
    
print(result)

'''
[입력 예시]
4 6
19 15 10 17
[출력 예시]
15
'''