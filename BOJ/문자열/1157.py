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
if len(lst) >= 2: print('?')
else: print(lst[0])

# 알파벳 개수만큼의 각 숫자에 대해 문자로 변환해 입력받은 문자열에서 각 문자의 개수를 세기

# word = input().upper()
# lst = []   # 모든 알파벳에 대해 입력받은 문자열에서 각 알파벳이 몇 개 있는지 개수 list
# for i in range(26):
#     lst.append(word.count(chr(i + 65)))
# # for i in range(26):
# #     print(chr(i + 65), end = ' ')
# max = lst[0]
# for i in range(len(lst)):
#     if lst[i] > max:
#         max = lst[i] 
#         cnt = i   # 최대일 때의 인덱스
# if lst.count(max) > 1: print('?')
# else: print(chr(65 + cnt))