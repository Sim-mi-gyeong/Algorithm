import time
start_time = time.time()

n = int(input())
data = []   # 각 공포도 
num = 0   # data에서 그룹이 설정하기 위해 빼낸 개수
cnt = 0   # 그룹 수 
for i in range(n):
    data.append(int(input()))
# data = list(map, input().split())

ans = len(data) - max(data)   # 우선, 결성 가능한 그룹의 수는 'data 개수 - data 중 최댓값' 일 것 

while(True):
    i = 0
    data.remove(data[i])
    i += 1
    num += 1
    if num == ans:
        ans = len(data) - max(data)
        cnt += 1
        break

end_time = time.time()
print('정답 : ', num)
print("걸린 시간 : ", end_time - start_time)
