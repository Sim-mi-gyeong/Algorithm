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
