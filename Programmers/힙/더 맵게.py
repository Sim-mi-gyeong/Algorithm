import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville:
        first = heapq.heappop(scoville)

        if first >= K:
            break

        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)

        answer += 1

        if len(scoville) == 1:
            if heapq.heappop(scoville) < K:
                return -1
            else:
                return answer

    return answer
