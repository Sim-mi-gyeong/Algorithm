n = input()
if len(n) == 1:
    n = "0" + n
next = int(n[0]) + int(n[1])  # 2 + 6 = 8
new = n[-1] + str(next)[-1]  # 6 8
cnt = 1
if n == new:
    print(cnt)
    exit(0)

while True:
    next = int(new[0]) + int(new[1])  # 6 + 8 = 14
    new = new[-1] + str(next)[-1]  # 8 4
    cnt += 1
    if new == n:
        break

print(cnt)

