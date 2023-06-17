def solution(users, emoticons):
    answer = [0, 0]
    data = [10, 20, 30, 40]
    discount = []

    def dfs(cnt, tmp):
        if cnt == len(tmp):
            discount.append(tmp[:])
            return
        else:
            for i in data:
                tmp[cnt] += i
                dfs(tmp, cnt + 1)
                tmp[cnt] -= i

    dfs([0] * len(emoticons), 0)

    for tmpDiscount in discount:
        cnt = 0
        get = 0
        for i in users:
            pay = 0
            for j in range(len(tmpDiscount)):
                if i[0] <= tmpDiscount[j]:
                    pay += emoticons[j] * (100 - tmpDiscount[j]) / 100
                if pay >= i[1]:
                    break
            if pay >= i[1]:
                pay = 0
                cnt += 1
            get += pay
        if cnt >= answer[0]:
            if cnt == answer[0]:
                answer[1] = max(answer[1], get)
            else:
                answer[1] = get
            answer[0] = cnt

    return answer
