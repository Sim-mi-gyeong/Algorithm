# 동전 0
import time
start_time = time.time()

n, k = map(int, input().split())
coin = []
cnt = 0
# for i in range(n):
#     coin.append(int(input()))
# coin = list(map(int, input().split()))   # 공백으로 받는 것이 아닌 줄 단위로 받음!
coin = [int(input()) for _ in range(n)]
coin.sort(reverse = True)

for i in coin:
    if k < i:
        pass
    else:
        cnt += (k // i)
        k %= i
        
end_time = time.time()
print(cnt)
print("걸린 시간 : ", end_time - start_time)