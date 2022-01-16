# 소트인사이드

# s = input()
# ans = ''
# lst = list()
# for i in s: lst.append(int(i))
# lst.sort(reverse=True)
# for i in lst: ans += str(i)
# print(ans)

s = sorted(list(input()), reverse=True)
ans = ''
for i in s: ans += i
print(ans)