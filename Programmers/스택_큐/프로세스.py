def solution(priorities, location):
    answer = 0

    val = [0] * len(priorities)
    val[location] = 1

    while True:
        if priorities[0] == max(priorities):
            answer += 1

            if priorities[0] == priorities[location] & val[0] == 1:
                break
            else:
                priorities.pop(0)
                val.pop(0)

        else:
            priorities.append(priorities[0])
            priorities.pop(0)
            val.append(val[0])
            val.pop(0)

    return answer


from collections import deque


def solution2(priorities, location):
    answer = 0

    q = deque()  # q = [(i,p) for i,p in enumerate(priorities)]
    for i in range(len(priorities)):
        q.append((i, priorities[i]))

    dic = dict()

    turn = 1
    while q:
        idx, priority = q.popleft()
        if q:
            high = max(q, key=lambda x: x[1])[1]
        # 마지막 남은 프로세스라면, 큐에서 꺼낸 후 빈 상태가 되므로 -> high 는 이전에 꺼낸 프로세스
        if len(q) > 0 and priority < high:
            q.append((idx, priority))
            continue
        if len(priorities) == 0:
            dic[idx] = turn

        dic[idx] = turn

        if location == idx:
            answer = turn
            break

        turn += 1

    return answer


def solution3(priorities, location):
    answer = 0

    process = dict()
    q = deque()
    priorities = deque(priorities)
    for i in range(len(priorities)):
        process[i] = priorities[i]
        q.append((i, priorities[i]))

    dic = dict()

    turn = 1
    while q:
        idx, priority = q.popleft()
        curr = priorities.popleft()
        if priorities:
            high = max(priorities)
        if len(priorities) > 0 and curr < high:
            q.append((idx, priority))
            priorities.append(curr)
            continue
        if len(priorities) == 0:
            dic[idx] = turn

        dic[idx] = turn

        if location == idx:
            answer = turn
            break

        turn += 1

    return answer
