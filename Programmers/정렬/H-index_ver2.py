def solution(citations):
    answer = 0
    n = len(citations)
    citations = sorted(citations)
    # x 보다 크거나 같은 수의 개수가 x 인 경우 -> h = x
    for i in range(n):
        if citations[i] >= n - i:  # 인용 수 >= 자기 자신보다 크거나 같은 개수
            answer = n - i
            return answer

    return 0


print(solution([3, 0, 6, 1, 5]))  # 3
print(solution([10, 10, 10, 10, 10]))  # 5
print(solution([0, 0, 0, 0, 0]))  # 0


"""
1) min(index,value) 부분은 가능할 수 있는 모든 h-index를 추출하는 부분 
2) max(~) 값은 가능할 수 있는 모든 h-index 중 가장 큰 값을 추출하는 부분
- 예를들어 [6, 5, 4, 1, 0]의 경우에선 min~ 부분은 min(1, 6), min(2, 5), min(3, 4), min(4, 1), min(5, 0), 
- 즉 해당 인용수 이상의 논문개수와 해당 논문의 인용수 중 더 작은 숫자를 고르는 작업을 하고(h-index로 가능한 숫자 추출),
- max~부분은 앞에서 골라진 (1, 2, 3, 1, 0) 중 가장 큰 숫자를 뽑아 실제 h-index를 구하는 방법
"""

