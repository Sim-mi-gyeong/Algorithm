def solution(n, times):
    answer = max(times) * n  # 최댓값으로 초기 -> 최솟값 구하기
    start, end = 1, max(times) * n

    while start <= end:
        mid = (start + end) // 2
        capa = 0
        for time in times:
            capa += mid // time
        if capa >= n:
            end = mid - 1
            if mid < answer:
                answer = mid
        else:
            start = mid + 1
    return answer
