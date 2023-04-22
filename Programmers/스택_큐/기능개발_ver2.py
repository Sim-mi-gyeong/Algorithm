# (p - 100) -> 음수,
# (p - 100) // s -> 내림한 음수(음수에서 내림은 절대값은 커짐),
# -((p - 100) // s) -> 올림한 양수
def solution(progresses, speeds):
    answer = []

    tmpDict = dict()
    for i in range(len(progresses)):
        prog, speed = progresses[i], speeds[i]
        remain = 100 - prog
        day = remain / speed  # int(remain / speed) : 소수점 버림

        # speed 가 1일 때 완료 일자 어떻게 계산했는지 확인
        # int type 체크로 할 경우, / 계산으로 인해 float => 10.0 / 11 로 값이 변경
        if remain % speed != 0:
            day = int(remain / speed) + 1

        if (i - 1) in tmpDict and (day <= tmpDict[i - 1]):
            tmpDict[i] = tmpDict[i - 1]
            continue

        tmpDict[i] = day

    deployDict = dict()
    for key, val in tmpDict.items():
        if val not in deployDict:
            deployDict[val] = 1
        else:
            deployDict[val] += 1

    answer = list(deployDict.values())

    return answer
