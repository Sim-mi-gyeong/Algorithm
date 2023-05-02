def solution(bridge_length, weight, truck_weights):
    answer = 0
    list = []
    bridge_length -= 1
    now_weight = 0
    idx = 0

    while True:
        if (now_weight + truck_weights[idx]) > weight:
            list.append(0)

        else:
            list.append(truck_weights[idx])
            now_weight += truck_weights[idx]
            idx += 1

        if len(list) > bridge_length:
            now_weight -= list.pop(0)

        answer += 1

        if idx == len(truck_weights):
            answer += bridge_length
            answer += 1
            break

    return answer


from collections import deque


def solution2(bridge_length, weight, truck_weights):
    answer = 0

    n = len(truck_weights)
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])

    time = 0
    currWeight = 0
    while len(truck_weights) or currWeight > 0:
        time += 1
        moveTruck = bridge.popleft()
        currWeight -= moveTruck

        if len(truck_weights) > 0 and currWeight + truck_weights[0] <= weight:
            currTruck = truck_weights.popleft()

            bridge.append(currTruck)
            currWeight += currTruck

        else:
            bridge.append(0)

    answer = time
    return answer
