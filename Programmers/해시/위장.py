# 서로 다른 옷의 조합의 수
from collections import defaultdict


def solution(clothes):
    answer = 0

    dic = defaultdict(list)
    for clothe in clothes:
        dic[clothe[1]].append(clothe[0])

    answer = 1
    for key, value in dic.items():
        answer *= len(dic[key]) + 1

    return answer - 1


print(
    solution(
        [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    )
)

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
