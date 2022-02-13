# 덩치
# 자기 자신보다 [키와 몸무게가 모두 큰 사람의 수 + 1] = 자기 자신 등수 

n = int(input())
lst = []
for i in range(n):
    x, y = map(int, input().split())
    lst.append([x, y])

cnt = 1
rank = []
for i in range(len(lst)):   # 자기 자신
    for j in range(len(lst)):   # 다른 사람
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]: cnt += 1
    rank.append(cnt)
    cnt = 1
for i in rank: print(i, end= ' ')