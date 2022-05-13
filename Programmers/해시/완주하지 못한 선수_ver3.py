def solution(participant, completion):
    answer = ""

    tmp = 0
    dic = dict()
    for i in participant:
        dic[hash(i)] = i
        tmp += hash(i)

    for j in completion:
        tmp -= hash(j)

    answer = dic[tmp]

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
