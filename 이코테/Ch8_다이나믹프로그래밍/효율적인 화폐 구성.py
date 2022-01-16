# 화폐 개수를 최소한으로 이용
# n : 화폐 종류  m : 만들고자 하는 금액
n, m = map(int, input().split())
c = []
for i in range(n): 
    # num = int(input())
    c.append(int(input()))

d = [0] * 10001

for i in range(2, m+1):
    for j in c:
        if i % j == 0:
            d[i] = min(d[i], d[i // j] + 1)
print(d[m])