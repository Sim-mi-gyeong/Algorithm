# 단어 수학
# 두 자리 개수가 다를 때
# GCF + ACDEB = 783 + 98654 = 99437 최대

n = int(input())
lst = [input() for _ in range(n)]
lst.sort(key=lambda x: len(x), reverse=True)
print(lst)


def wordCount(word, tmp):
    maxIdx = 9
    idx = maxIdx
    for j in word:
        while visited[idx] and idx > 0:
            idx -= 1
        if not visited[idx]:
            visited[idx] = 1
            if j in dic:
                tmp += str(dic[j])
            else:
                dic[j] = idx
                tmp += str(dic[j])

    print(tmp)
    return int(tmp)


visited = [0] * 10  # 0 ~ 9
dic = dict()  # {A : 9, B : 8, ... }


# maxIdx = 9
# idx = maxIdx
ans = 0
val = 0

for i in lst:
    tmp = ""
    # 백트래킹
    val += wordCount(i, tmp)
    ans = max(ans, val)

    # visited[idx] = 0
    # tmp = int(tmp)
    # tmp -= dic[j]
    # del dic[j]
    # tmp = str(tmp)

    # print(tmp)
    # val += int(tmp)
    # ans = max(ans, val)

print(dic)
print(ans)


'''
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB
1790

'''