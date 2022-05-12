# 강의실 배정

n = int(input())
# 시작 시간 기준 정렬 X -> 끝나는 시간 기준
# 최소의 강의식 수 + 모든 수업 가능


lst = [list(map(int, input().split())) for _ in range(n)]
lst = sorted(lst, key=lambda x: x[1])
cnt = 0
minValue = 1e9
for i in range(len(lst) - 1):
    endBefore, startAfter = lst[i][1], lst[i + 1][0]
    if endBefore > startAfter:
        cnt += 1
    minValue = min(minValue, cnt)

print(cnt)
