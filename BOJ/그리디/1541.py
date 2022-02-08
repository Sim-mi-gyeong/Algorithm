# 잃어버린 괄호
# 다시
# - 바로 뒤에서 -> - 발견하면 괄호
s = input()
s = s.split('-')
sum = 0
# for i in range(len(s)):
#     if '+' in s[i]:
#         s[i] = s[i].split('+')
#         for j in s[i]:
#             sum += int(j)
#         s[i]= sum

# cnt = 0
# for i in s[1:]:
#     cnt += int(i)
# ans = int(s[0]) - cnt
# print(ans)

# - 보다 앞에 있던 숫자들로 이루어진 원소에 대해 + 기준으로 split 해서 합 구하기
for i in s[0].split('+'):
    sum += int(i)

# - 보다 두에 있던 숫자들로 이루어진 원소에 대해 + 기준으로 split 한각 원소를 앞에서 구한 sum 에서 빼주기
for j in s[1:]:
    for k in j.split('+'):
        sum -= int(k)
print(sum)