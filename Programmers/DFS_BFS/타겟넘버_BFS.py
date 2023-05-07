from collections import deque


def solution(numbers, target):
    global n
    answer = 0
    n = len(numbers)

    q = deque([(numbers[0], 0), (-numbers[0], 0)])

    while q:
        val, idx = q.popleft()
        idx += 1
        if idx < n:
            q.append((val + numbers[idx], idx))
            q.append((val - numbers[idx], idx))
        else:
            if val == target:
                answer += 1

    return answer
