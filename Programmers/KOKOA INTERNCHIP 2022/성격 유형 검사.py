def solution(survey, choices):
    answer = ""
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for idx, surv in enumerate(survey):
        if choices[idx] == 4:
            continue
        elif 1 <= choices[idx] <= 3:
            dic[surv[0]] += 4 - choices[idx]
        else:
            dic[surv[1]] += choices[idx] - 4

    if dic["R"] >= dic["T"]:
        answer += "R"
    else:
        answer += "T"

    if dic["C"] >= dic["F"]:
        answer += "C"
    else:
        answer += "F"

    if dic["J"] >= dic["M"]:
        answer += "J"
    else:
        answer += "M"

    if dic["A"] >= dic["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer
