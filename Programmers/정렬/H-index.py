def solution(citations):
    answer = 0
    n = len(citations)
    citations = sorted(citations, reverse=True)

    maxValue = citations[0]
    for i in range(maxValue):
        cnt1, cnt2 = 0, 0
        for j in range(n):
            if citations[j] >= i:
                cnt1 += 1
            else:
                cnt2 += 1
        if i <= cnt1 and i >= cnt2:
            answer = max(answer, i)

    return answer


print(solution([3, 0, 6, 1, 5]))  # 3
print(solution([10, 10, 10, 10, 10]))  # 5
print(solution([0, 0, 0, 0, 0]))  # 0
