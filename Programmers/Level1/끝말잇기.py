def solution(n, words):
    fail = False
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1]:
            num = (i % n) + 1
            turn = (i // n) + 1
            fail = True
            break

        if words[i] in words[:i]:
            num = (i % n) + 1
            turn = (i // n) + 1
            fail = True
            break

    if fail == False:
        num, turn = 0, 0

    answer = [num, turn]
    return answer
