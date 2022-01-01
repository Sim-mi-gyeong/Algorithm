data = input()
alpha = []
num = []
for i in data:
    if i.isalpha():
        alpha.append(i)
    else:
        num.append(int(i))
ans=''
for i in sorted(alpha):   # ''.join()
    ans += i
if sum(num) != 0:
    ans += str(sum(num))
print(ans)

# 만약, 숫자가 하나도 없을 때, 즉 합이 0일때도 출력되므로 숫자 존재 여부도 확인해야함!