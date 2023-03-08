# 카드 놓기

from itertools import combinations

n = int(input())
k = int(input())  # 선택할 카드 수
lst = [map(int, input().split()) for _ in range(n)]
combList = list(combinations(lst, k))
combSet = set(combinations(lst, k))
strList = []
for comb in combList:
    string = ""
    for s in comb:
        string += str(s)
    strList.append(string)

strList = set(strList)
# print("strList : ", strList)
# print("combList : ", combList)
# print("combSet : ", combSet)
ans = len(strList)
print(ans)
