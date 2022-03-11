# 공유기 설치
# 설치할 수 있는 공유기 개수 > c -> 더 넓게 설치 가능 -> 설치 거리 mid + 1
# 설치할 수 있는 공유기 개수 < c -> 더 좁게 설치 -> 설치 거리 mid - 1

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
 # for 문 실행마다 거리의 최솟값들 중 가장 큰 값 저장
start = 1
end = lst[-1] - lst[0]
# ans = 0   # 정답으로 기록할, 각 조합에서 설치 거리의 최댓값 저장
def binarySearch(lst, start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 1   
        startX = lst[0]

        for i in range(1, n):
            if lst[i] >= startX + mid:   # 시작 위치 + mid 거리 만큼에 설치 가능한 경우
                cnt += 1
                startX = lst[i]   # 시작 위치 재설정
        if cnt >= c:
            start = mid + 1
            ans = mid   # 각 조합에서 설치 거리
        else:
            end = mid - 1
    return ans

print(binarySearch(lst, start, end))