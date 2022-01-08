word = input().upper()
dic = {}
for i in word:
    if i not in dic.keys():
        dic[i] = 0
    dic[i] += 1
cnt = max(dic.values())
lst = []
for i, j in dic.items():
    if j == cnt:
        lst.append(i)
if len(lst) >= 2:
    print('?')
else:
    print(lst[0])



# print(cnt)
# if len(cnt) >= 2:
#     print('?')
# else:
#     for i, j in dic.items():
#         if j == cnt[0]: print(i)
