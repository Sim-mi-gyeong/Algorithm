# 통계학

import collections
import sys

input = sys.stdin.readline

n = int(input())
lst = []
dic = dict()
for _ in range(n):
    num = int(input())
    lst.append(num)
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1


lst.sort()
sumVal = int(round(sum(lst) / n, 0))
ran = lst[-1] - lst[0]
centerVal = lst[n // 2]
counter_lst = collections.Counter(lst).most_common()

# if len(counter_lst) > 1:
#     if counter_lst[0][1] == counter_lst[1][1]:
#         maxCountVal = counter_lst[1][0]
#     else:
#         maxCountVal = counter_lst[0][0]

# else:
#     maxCountVal = counter_lst[0][0]

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

if len(dic) > 1:
    if dic[0][1] == dic[1][1]:
        maxCountVal = dic[1][0]
    else:
        maxCountVal = dic[0][0]
else:
    maxCountVal = dic[0][0]


print(sumVal)
print(centerVal)
print(maxCountVal)
print(ran)
