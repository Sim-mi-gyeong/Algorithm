def solution(citations):
    citations = sorted(citations, reverse=True)
    answer = max(max(min, enumerate(citations, start=1)))
    return answer


print(solution([3, 0, 6, 1, 5]))  # 3
print(solution([10, 10, 10, 10, 10]))  # 5
print(solution([0, 0, 0, 0, 0]))  # 0

"""
1) min(index,value) : 가능한 모든 h-index를 추출
- 예를들어 [6, 5, 4, 1, 0]의 경우에선 min~ 부분은 min(1, 6), min(2, 5), min(3, 4), min(4, 1), min(5, 0), 
- 즉 (해당 인용수 이상의 논문 개수, 해당 논문의 인용수) 중 더 작은 숫자를 고르기
2) max() : 가능한 모든 h-index 중 가장 큰 값을 추출
- 앞에서 골라진 (1, 2, 3, 1, 0) 중 가장 큰 숫자를 뽑아 -> 실제 h-index를 구하는 방법
"""
