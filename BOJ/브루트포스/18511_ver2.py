# 큰 수 구성하기

n, k = input().split()
lst = list(input().split())
ans = 0

flag = False
l = len(n)
lst.sort()


def get_minimum_l():
    return lst[-1] * l


if get_minimum_l() > n:
    if l == 1:
        print(-1)
    else:
        print(lst[0] * (l - 1))
    exit()

ans = []
for i in range(l):
    if flag:
        ans.append(lst[0])
    elif n[i] > lst[0]:
        ans.append(lst[0])
        flag = True
    elif n[i] == lst[0]:
        ans.append(lst[0])
    elif n[i] > lst[1]:
        pass
