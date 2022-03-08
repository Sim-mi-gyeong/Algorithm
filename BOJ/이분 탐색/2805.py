# 나무 자르기
# 같은 반복문을 함수 내부에서 -> 시간 초과 해결
# https://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
# lst.sort()
start = 0
end = max(lst)

def binarySearch(lst, m, start, end):
    while start <= end:
        tmpSum = 0
        mid = (start + end) // 2
        for i in lst:
            if i > mid:
                tmpSum += (i-mid)
        # 자른 길이 합이 조건 만족 -> 정답 저장, 오른쪽 탐색
        if tmpSum >= m:
            maxH = mid
            start = mid + 1
        else:
            end = mid - 1

    return maxH

print(binarySearch(lst, m, start, end))