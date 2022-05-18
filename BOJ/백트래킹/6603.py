# 로또

from itertools import combinations

while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    lst = lst[1:]
    comList = list(combinations(lst, 6))
    comList = sorted(comList)
    for com in comList:
        print(*com)
    print()

