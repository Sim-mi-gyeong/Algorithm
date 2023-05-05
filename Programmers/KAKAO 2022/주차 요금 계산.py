def solution(fees, records):
    answer = []

    basicTime, basicCost, unitTime, unitCost = (
        int(fees[0]),
        int(fees[1]),
        int(fees[2]),
        int(fees[3]),
    )
    # 각 차량별로, 입차 - 출차 시간 기록
    # {num : [{"in" : "시간", "out" : "시간"}, {"in" : "시간", "out" : "시간"}] }
    dic = dict()
    # 나갔다가 다시 들어오는 경우 존재
    for record in records:
        time, num, act = record.split(" ")
        # 최초 입차인 경우
        if num not in dic and act == "IN":
            dic[num] = [{act: time}]

        # 출차 후 재입차인 경우
        elif num in dic and "IN" in dic[num][-1] and act == "IN":
            dic[num].append({act: time})

        # 최초 출차인 경우
        elif len(dic[num]) == 1 and act == "OUT":
            dic[num][0][act] = time

        # 두번째 이후 출차인 경우
        elif len(dic[num]) > 1 and act == "OUT":
            dic[num][-1][act] = time

    # 번호가 작은 순서대로 정렬
    dic = dict(sorted(dic.items()))

    for key, val in dic.items():
        totalDiff = 0
        # 각 차량 번호마다, 출차 시간이 없는 경우 23:59 로
        for tmpVal in val:
            inTime = tmpVal["IN"]
            if "OUT" not in tmpVal:
                outTime = "23:59"
            else:
                outTime = tmpVal["OUT"]

            # 누적 시간 계산
            # 시간을 분으로 환산해서 계산
            inTimeH, inTimeM = int(inTime.split(":")[0]), int(inTime.split(":")[1])
            outTimeH, outTimeM = int(outTime.split(":")[0]), int(outTime.split(":")[1])

            inTimeMin = 60 * inTimeH + inTimeM
            outTimeMin = 60 * outTimeH + outTimeM

            diff = outTimeMin - inTimeMin

            totalDiff += diff

        # 기본 시간 미만인 경우
        if totalDiff <= basicTime:
            totalCost = basicCost
        else:
            # 추가 주차한 시간
            moreTime = totalDiff - basicTime
            # 단위 시간으로 나누어 떨어지지 않는 경우 올림
            moreUnit = moreTime / unitTime
            if moreTime % unitTime != 0:
                moreUnit = int(moreUnit) + 1

            moreCost = moreUnit * unitCost
            totalCost = basicCost + moreCost

        answer.append(totalCost)

    return answer
