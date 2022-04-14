def solution(land):

    for i in range(1, len(land)):
        for j in range(4):
            maxValue = -1e9
            for k in range(4):
                if j != k:
                    maxValue = max(maxValue, land[i - 1][k])
            land[i][j] += maxValue

    answer = max(land[-1])
    return answer
