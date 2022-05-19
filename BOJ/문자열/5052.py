# 전화번호 목록

t = int(input())
for _ in range(t):
    check = True
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    lst = sorted(lst)

    for i in range(len(lst[:-1])):
        if lst[i + 1].startswith(lst[i]):
            check = False

    if check:
        print("YES")
    else:
        print("NO")
