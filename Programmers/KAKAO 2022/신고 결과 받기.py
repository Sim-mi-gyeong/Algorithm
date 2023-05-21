def solution(id_list, report, k):
    answer = []
    # 각 유저별, {name : {신고당한 횟수 : 0, 해당 유저를 신고한 유저} }
    reportDic = dict()
    userDic = dict()
    for id in id_list:
        reportDic[id] = {"num": 0, "userList": []}
        userDic[id] = 0

    for rep in report:
        reportUser, targetUser = rep.split()[0], rep.split()[1]
        # 동일한 유저에 대한 신고 횟수는 1회로 처리
        if reportUser in reportDic[targetUser]["userList"]:
            continue
        reportDic[targetUser]["num"] += 1
        reportDic[targetUser]["userList"].append(reportUser)

    for key, val in reportDic.items():
        # val["num"] >= k 인 경우, userList 에 포함된 유저들에게 각각 신고 확인 알림
        if val["num"] >= k:
            for reportUser in val["userList"]:
                userDic[reportUser] += 1

    answer = list(userDic.values())
    return answer
