# 일곱 난쟁이

lst = []
for i in range(9): lst.append(int(input()))
lst.sort()
rent = sum(lst) - 100
# 2 명의 합이 40인 경우 그 2명 제거
for i in range(len(lst)-1):
    for j in range(1, len(lst)):
        if lst[i] + lst[j] == rent:
            if lst[i] == lst[j]:
                continue
            else: a, b = lst[i], lst[j]
lst.remove(a), lst.remove(b)
for i in lst: print(i)