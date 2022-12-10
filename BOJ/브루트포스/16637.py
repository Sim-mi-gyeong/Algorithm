# 괄호 추가하기
# 괄호의 최대 개수는, 숫자 개수 // 2
import sys

input = sys.stdin.readline
n = int(input().rstrip())
lst = input().rstrip()
num = int(round(n / 2, 0))
maxCnt = num // 2
print("lst : ", lst)
print("num : ", num)
print("maxCnt : ", maxCnt)

kind = ["+", "-", "*"]
lst1, lst2 = [], []
for i in lst:
    if i in kind:
        lst2.append(i)
    else:
        lst1.append(int(i))
print("lst1 : ", lst1)
print("lst2 : ", lst2)

INF = 1e9
ans = -1 * INF  # -2 ** 31 - 1
useUn = False

# for i in range(len(lst1) - 1):
i = 0
while i <= len(lst1) - 1:
    i = 0
    if lst2[i] == "+":
        tmp1 = lst1[i] + lst1[i + 1]
        lst1.remove(lst1[0])
        lst1.remove(lst1[0])
        lst1.insert(i, tmp1)
        lst2.remove(lst2[0])

    elif lst2[i] == "*":
        tmp2 = lst1[i] * lst1[i + 1]
        lst1.remove(lst1[0])  # lst1.pop(lst1[0])
        lst1.remove(lst1[0])
        lst1.insert(i, tmp2)
        lst2.remove(lst2[0])

    elif lst2[i] == "-":
        tmp2 = lst1[i] - lst1[i + 1]
        lst1.remove(lst1[0])
        lst1.remove(lst1[0])
        lst1.insert(i, tmp2)
        lst2.remove(lst2[0])

    print(lst1)

    if len(lst1) == 1:
        break


print(lst1)
