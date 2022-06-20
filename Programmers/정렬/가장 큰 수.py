# from itertools import permutations   # 시간초과
from functools import cmp_to_key


def comparator(x, y):
    o1 = x + y
    o2 = y + x
    return (int(o1) > int(o2)) - (int(o1) < int(o2))  # o1이 크다면 1 / o2가 크다면 -1 / 같으면 0


def solution(numbers):
    arr = [str(i) for i in numbers]
    arr = sorted(arr, key=cmp_to_key(comparator), reverse=True)
    answer = str(int("".join(arr)))  # str > int : 0000 -> 0
    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))


"""
return 음수 : 먼저 들어온 요소가 앞으로
return 0 : 바뀌지 X
return 양수 : 나중에 들어온 요소가 앞으로
"""

