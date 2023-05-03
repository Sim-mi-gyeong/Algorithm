def solution(nums):
    answer = 0

    n = len(nums)
    dic = dict()
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    if len(dic) <= n // 2:
        answer = len(dic)
    else:
        answer = n // 2
    return answer
