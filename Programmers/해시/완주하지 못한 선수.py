from collections import Counter


def solution(participant, completion):
    answer = ""
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    answer = participant[len(participant) - 1]

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
