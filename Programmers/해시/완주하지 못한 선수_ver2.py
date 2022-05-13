from collections import Counter


def solution(participant, completion):
    answer = ""

    answer = (Counter(participant) - Counter(completion)).keys()
    answer = list(answer)[0]

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
