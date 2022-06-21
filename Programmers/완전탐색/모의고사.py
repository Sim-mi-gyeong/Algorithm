def solution(answers):
    answer = []
    cnt1, cnt2, cnt3 = 0, 0, 0
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [2, 1, 2, 3, 2, 4, 2, 5]
    lst3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, ans in enumerate(answers):
        if ans == lst1[i % len(lst1)]:
            cnt1 += 1
        if ans == lst2[i % len(lst2)]:
            cnt2 += 1
        if ans == lst3[i % len(lst3)]:
            cnt3 += 1

    result = [cnt1, cnt2, cnt3]
    maxVal = max(result)
    answer = [i + 1 for i, v in enumerate(result) if v == maxVal]

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))

