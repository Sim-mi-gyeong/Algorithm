# 더하기 사이클

s = input()
if len(s) == 1: s = '0' + s
next = int(s[0]) + int(s[-1])
new = s[-1] + str(next)[-1]
cnt = 1
if new == s: 
    print(cnt)
    exit(0)
while True:
    next = int(new[0]) + int(new[-1])
    ans = str(new)[-1] + str(next)[-1]
    new = ans
    cnt += 1
    if ans == s: break
print(cnt)