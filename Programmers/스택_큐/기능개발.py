def solution(progresses, speeds):
    answer = []
    prog = list(reversed(progresses))
    spd = list(reversed(speeds))

    while True:
        for i in range(len(prog)):
            prog[i] += spd[i]

        cnt = 0

        while prog[-1] >= 100:
            prog.pop()
            cnt += 1

            if not prog:
                break

        if cnt != 0:
            answer.append(cnt)

        if len(prog) == 0:
            break

    return answer
