from itertools import product


def solution(word):
    answer = 0
    lst = ["A", "E", "I", "O", "U"]
    result = []
    for i in range(1, 6):
        for s in product(lst, repeat=i):
            result.append("".join(s))

    result.sort()
    answer = result.index(word) + 1

    return answer
