import math
from itertools import permutations


def prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    arr = [i for i in numbers]
    permList = []
    for i in range(1, len(numbers) + 1):
        permList += list(set(permutations(arr, i)))

    newArr = list(set([int("".join(perm)) for perm in permList]))

    for i in newArr:
        if prime(i):
            answer += 1
    return answer


print(solution("17"))
print(solution("011"))
