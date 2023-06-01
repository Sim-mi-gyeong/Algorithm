def solution(n, lost, reserve):
    answer = n - len(lost)

    for i in range(len(reserve)):
        front = reserve[i] - 1
        back = reserve[i] + 1
        if front in lost:
            lost.remove(front)
            answer += 1
            continue
        if back in lost:
            lost.remove(back)
            answer += 1
        else:
            continue
    return answer
