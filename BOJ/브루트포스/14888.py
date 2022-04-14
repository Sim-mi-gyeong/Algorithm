# 연산자 끼워넣기

from itertools import permutations  # 순열 -> 같은 것을 다른 것으로 처리

n = int(input())
lst = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
op = dict()
op["+"], op["-"], op["*"], op["//"] = plus, minus, mul, div

opList = []
for key, value in op.items():
    if value != 0:
        for i in range(1, value + 1):
            opList.append(key)

opPerList = list(permutations(opList, len(opList)))
opPerList = list(set(opPerList))

minAns = 1e9
maxAns = -1 * 1e9
for subOp in opPerList:
    lstCopy = lst.copy()
    while len(lstCopy) != 1:
        for j in subOp:
            a = lstCopy.pop(0)
            b = lstCopy.pop(0)
            if j == "+":
                tmp = a + b

            elif j == "-":
                tmp = a - b

            elif j == "*":
                tmp = a * b

            elif j == "//":
                if a < 0 and b > 0:
                    a = -1 * a
                    tmp = -1 * (a // b)
                elif b < 0 and a > 0:
                    b = -1 * b
                    tmp = -1 * (a // b)
                else:
                    tmp = a // b

            lstCopy.insert(0, tmp)

        if len(lstCopy) == 1:
            break

    # print("lst : ", lstCopy)
    tmpCal = lstCopy[0]
    minAns = min(minAns, tmpCal)
    maxAns = max(maxAns, tmpCal)

print(maxAns)
print(minAns)


"""
2
-9 3
"""

