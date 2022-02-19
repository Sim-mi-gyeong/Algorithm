# 더하기 사이클

s = input()
next = int(s[0]) + int(s[-1])   # 8
new = s[-1] + str(next)[-1]   # 68

cnt = 0
while True:
    # next = int(s[0]) + int(s[-1])   # 정수 2 + 6 = 8 / 6 + 8 = 14
    next = int(new[0]) + int(new[-1])   # 14
    print('next : ', next)
    ans = str(next)[-1] + str(new)[-1]
    print('ans : ', ans)
    cnt += 1
    if ans == s: break
print(cnt)