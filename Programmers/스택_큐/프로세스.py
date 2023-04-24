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
