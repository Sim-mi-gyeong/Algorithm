# 회의실 배정
n = int(input())

# time = [tuple(map(int, input().split()) for _ in range(n))]
list = []
cnt = 1
max = cnt
for i in range(n):
    start, end = map(int, input().split())
    list.append((start, end))
list.sort()   # 튜플 정렬 시 default 값은 튜플의 첫 번째 인자 기준
# [(0, 6), (1, 4), (2, 13), (3, 5), (3, 8), (5, 7), (5, 9), (6, 10) (8, 11), (8, 12), (12, 14)]
# for i in range(len(list[:-1])):
#     if (list[i][1] - list[i][0]) > (list[i+1][1] - list[i+1][0]):
#         pass
#     else:
#         if list[i][1] > list[i+1][0]:
#             pass
#         else:
#             cnt += 1 

# for i in range(len(list)):
#     for j in range(1, len(list)):
#         if list[i][1] > list[j][0]:
#             pass
#         else:
#             cnt += 1
#             i += j
i = 0
j = i + 1
incre = 1
# while(True):
#     # cnt = 1
#     while(i < len(list) - 1):
#         if list[i][1] > list[j][0]:
#             j += 1
#             if j == len(list) - 1:
#                 i += 1
#         if list[i][1] <= list[j][0]:
#             cnt += 1
#             i = j
#             j = i + 1
#         # i += 1
#         # j = i + 1
#     if max < cnt:
#         max = cnt

# while(i < len(list) - 1):
#     # if max <= cnt:
#     #     cnt = 1
#     if list[i][1] > list[j][0]:
#         j += 1
#         if j == len(list) - 1:
#             i += 1
#     # if list[i][1] <= list[j][0]:
#     else:
#         cnt += 1
#         i = j
#         j = i + 1
#         # i += 1
#         # j = i + 1
#     # max = cnt

#     if i == len(list) - 1:
#         i += 1

while(incre <= len(list) - 1):
    # if max <= cnt:
    #     cnt = 1
    if list[i][1] > list[j][0]:
        # if j < len(list) - 1:
        if j == len(list) - 1:
            if max < cnt:
                max = cnt

            i = incre
            j = i + 1
            incre += 1
            cnt = 1
        else:
            j += 1
    else:
        cnt += 1
        i = j
        if i == len(list) - 1:
            if max < cnt:
                max = cnt

            i = incre
            j = i + 1
            incre += 1
            cnt = 1
        else:
            j = i + 1
            # if j == len(list) - 1:
            #     if max < cnt:
            #         max = cnt

            #     i = incre
            #     j = i + 1
            #     incre += 1
            #     cnt = 1
            # else:
            #     j = i + 1
        # i += 1
        # j = i + 1
    # max = cnt
    
print(cnt)    
print(max)