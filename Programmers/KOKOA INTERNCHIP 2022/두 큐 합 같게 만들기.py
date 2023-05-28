from collections import deque


def solution(queue1, queue2):
    answer = -1
    queue1, queue2 = deque(queue1), deque(queue2)
    q1Sum, q2Sum = sum(queue1), sum(queue2)

    # 두 큐의 합을 같게 만들 수 없는 경우
    if (q1Sum + q2Sum) % 2 == 1:
        return -1

    maxVal, cnt = 3 * len(queue1), 0
    while True:
        if cnt >= maxVal:
            return -1
        if q1Sum > q2Sum:
            tmp = queue1.popleft()
            q1Sum -= tmp
            queue2.append(tmp)
            q2Sum += tmp
            cnt += 1

        elif q1Sum < q2Sum:
            tmp = queue2.popleft()
            q2Sum -= tmp
            queue1.append(tmp)
            q1Sum += tmp
            cnt += 1
        else:
            break

    answer = cnt

    return answer
