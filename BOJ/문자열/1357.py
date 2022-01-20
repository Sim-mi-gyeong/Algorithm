# 뒤집힌 덧셈

x, y = input().split()
sum = int(x[::-1]) + int(y[::-1])
ans = (str(sum))[::-1]
if ans[0] == '0': print(int(ans[1:]))
else: print(int(ans))