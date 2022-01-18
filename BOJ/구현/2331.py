# 반복 수열

a, p = map(int, input().split())
lst = [int(i) for i in str(a)]
s = [a]
sum = 0

while True:
    for i in lst: sum += i ** p
    if sum in s:
        # 해당 수부터 ~ 리스트 마지막 원소까지 제거
        idx = s.index(sum)
        s = s[:idx]
        break
    else:
        s.append(sum)
        lst = [int(i) for i in str(s[-1])]
    sum = 0
print(len(s))