# 영화감독 숌

n = int(input())
target = "666"
i = 0
cnt = 0
while True:
    i += 1
    if target in str(i):
        cnt += 1
        if cnt == n:
            print(i)
            break
