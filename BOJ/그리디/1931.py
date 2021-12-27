# 회의실 배정
n = int(input())

# time = [tuple(map(int, input().split()) for _ in range(n))]
list = []
cnt = 0
max = 0
for i in range(n):
    start, end = map(int, input().split())
    list.append((start, end))
list.sort()   # 튜플 정렬 시 default 값은 튜플의 첫 번째 인자 기준
# [(0, 6), (1, 4), (2, 13), (3, 5), (3, 8), (5, 7), (5, 9), (6, 10), (8, 11), (8, 12), (12, 14)]
for i in range(len(list[:-1])):
    if list[i][1] > list[i+1][0]:
        pass
    else:
        cnt += 1 

print(cnt)