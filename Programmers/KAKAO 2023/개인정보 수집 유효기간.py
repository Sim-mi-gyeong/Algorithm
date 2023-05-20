def solution(today, terms, privacies):
    answer = []

    termDic = dict()
    for term in terms:
        term = term.split()
        kind, month = term[0], term[1]
        termDic[kind] = int(month)

    for idx, privacy in enumerate(privacies):
        privacy = privacy.split()
        date, kind = privacy[0], privacy[1]
        date = date.split(".")
        year, month, day = int(date[0]), int(date[1]), int(date[2])

        if month + termDic[kind] > 12:
            unitYear = termDic[kind] // 12
            unitMonth = termDic[kind] - 12 * unitYear
            year += unitYear
            if month + unitMonth > 12:
                year += 1
                month = month + unitMonth - 12
            else:
                month += unitMonth
        else:
            month += termDic[kind]

        if day - 1 == 0:
            day = 28
            month -= 1
        else:
            day -= 1

        strYear = str(year)
        strMonth = str(month).zfill(2)
        strDay = str(day).zfill(2)
        afterDate = strYear + "." + strMonth + "." + strDay
        if afterDate < today:
            answer.append(idx + 1)

    return answer
