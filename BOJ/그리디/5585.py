# 거스름돈

coin = [500, 100, 50, 10, 5, 1]
cnt = 0
a = int(input())
re = 1000 - a

for i in coin:
    cnt += re // i
    re %= i

print(cnt)
