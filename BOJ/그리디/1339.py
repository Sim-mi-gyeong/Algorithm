# 단어수학

n = int(input())
lst = [input() for _ in range(n)]

dic = dict()
for i in range(len(lst)):
    for j in range(len(lst[i])):
        alpha = lst[i][j]
        if not alpha in dic:
            dic[alpha] = 10 ** (len(lst[i]) - j - 1)
        else:
            dic[alpha] += 10 ** (len(lst[i]) - j - 1)

dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
ans = 0
maxVal = 9
for k, v in dic.items():
    ans += v * maxVal
    maxVal -= 1

print(ans)
