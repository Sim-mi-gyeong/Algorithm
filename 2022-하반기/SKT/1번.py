def solution(logs, events):
    answer = []

    # register -> clearTutorial -> clearBattle -> getReward 단계로 로그 찍혀야 함
    dic = dict()
    for log in logs:
        log = log.split()
        time, user, action = log[0], log[1], log[2]
        if user not in dic:
            dic[user] = [action]
        else:
            dic[user].append(action)

    for key, val in dic.items():
        # 1. 유저의 진행 이벤트가 중복된 것은 없는지
        # val 을 set 처리한 원소 개수와 val 원소 개수가 다르면 -> 중복된 것
        setVal = set(val)
        if len(setVal) != len(val):
            answer.append(key)
            continue

        # 2. 유저의 진행 이벤트가 모두 events 개수만큼 있는지

        # 3. 유저의 진행 이벤트가 모두 events 순서대로 있는지
        for i in range(len(val)):
            if val[i] != events[i]:
                answer.append(key)
                break
    # 불법 사용 유저 X -> "-1"(문자열 리턴)
    if len(answer) == 0:
        answer = ["-1"]
    # 불법 사용 유저 id 사전 순 정렬
    answer = sorted(answer)

    return answer
