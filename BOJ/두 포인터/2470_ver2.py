# 두 용액
# 시간 초과 -> 이진탐색으로 풀기

import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort()

# 정답 처리
if n == 2: 
    print(lst[0], lst[1])
    exit(0)

start = 0
end = max(lst)
minD = 2000000001

for i in range(n-1):
    start = i+1
    end = n-1
    
    while start <= end:
        mid = (start + end) // 2
        tmpSum = lst[i] + lst[mid]

        # 기존에 저장된 차이 값보다 해당 연산의 결과가 0과 더 가까워진다면, 
        if abs(tmpSum) < minD:
            # 해당 값을 저장
            ans1, ans2, minD = i, mid, abs(tmpSum)
        # 혼합 특성 값 < 0 -> 더 큰 값 필요
        if tmpSum < 0:
            start = mid + 1
        # 혼합 특성 값 > 0 -> 더 작은 값 필요
        else:
            end = mid - 1

print(lst[ans1], lst[ans2])