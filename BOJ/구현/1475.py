# 방 번호
n = input()

check = [0] * 10
for i in range(len(n)):
    num = int(n[i])
    if num != 6 and num != 9:
        check[num] += 1
    elif num == 6 or num == 9:
        if check[6] < check[9]:
            check[6] += 1
        else:
            check[9] += 1

cnt = max(check)
print(cnt)
