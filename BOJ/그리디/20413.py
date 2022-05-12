# MVP 다이아몬드 (Easy)

n = int(input())
s, g, p, d = map(int, input().split())
c = input()
# sum은 계속 누적되는 값, 이전 값을 알아야 함
ans, back = 0, 0
# 그 다음 등급 최소 금액 - 1 - (이전 금액 = (i번째 금액 - i-1 번째 금액))
for i in range(len(c)):
    if c[i] == "B":
        ans += s - 1 - back
        back = s - 1 - back
    elif c[i] == "S":
        ans += g - 1 - back
        back = g - 1 - back
    elif c[i] == "G":
        ans += p - 1 - back
        back = p - 1 - back
    elif c[i] == "P":
        ans += d - 1 - back
        back = d - 1 - back
    elif c[i] == "D":
        ans += d
        back = d

print(ans)
