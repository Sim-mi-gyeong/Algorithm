from itertools import permutations


def solution(k, dungeons):
    answer = -1

    lst = [i for i in range(1, len(dungeons) + 1)]
    perm = list(permutations(lst, len(lst)))

    maxCount = 0

    for tmp in perm:
        cnt = 0
        initPower = k

        for i in tmp:
            thisDungeon = dungeons[i - 1]
            tmpInitPower, tmpMinusPower = thisDungeon[0], thisDungeon[1]

            if initPower < tmpInitPower:
                break
            initPower -= tmpMinusPower
            cnt += 1

        if maxCount < cnt:
            maxCount = cnt

    answer = maxCount
    return answer
