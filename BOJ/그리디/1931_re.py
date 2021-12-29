# 회의실 배정
import time
start_time = time.time()

n = int(input())

list = []
for i in range(n):
    start, end = map(int, input().split())
    list.append((start, end))
list.sort() 

i = 0
j = i + 1
incre = 1
cnt = 1
max = cnt

while(incre <= len(list) - 1):
    if list[i][1] > list[j][0]:
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

end_time = time.time()
print(max)
print('걸린 시간 : ', end_time - start_time)