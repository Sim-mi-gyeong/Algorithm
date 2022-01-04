# 회의실 배정
# O(N) -> '가장 일찍 끝나는 회의의 종료 시각' <= '다음 회의의 시작 시각'

time = [list(map(int, input().split())) for _ in range(int(input()))]
time.sort(key = lambda x: (x[1], x[0]))
cnt = 1 
start = time[0][0]
end = time[0][1]

for i in range(1, len(time)):
    if time[i][0] >= end:
        start = time[i][0]
        end = time[i][1]
        cnt += 1
print(cnt)