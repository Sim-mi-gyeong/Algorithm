# 전화번호 목록

t = int(input())
for _ in range(t):
    check = True
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    lst = sorted(lst)

    for p1, p2 in zip(lst, lst[1:]):
        if p2.startswith(p1):
            check = False

    if check:
        print("YES")
    else:
        print("NO")
