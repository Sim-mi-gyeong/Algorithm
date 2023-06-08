def solution(cap, n, deliveries, pickups):
    answer = 0

    tmpDeiveries, tmpPickups = 0, 0
    for i in range(n):
        tmpDeiveries += deliveries[n - i - 1]
        tmpPickups += pickups[n - i - 1]

        while tmpDeiveries > 0 or tmpPickups > 0:
            tmpDeiveries -= cap
            tmpPickups -= cap

            answer += (n - i) * 2

    return answer
