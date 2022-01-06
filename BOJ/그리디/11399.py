# ATM
# 시간이 적게 걸리는 사람이 앞으로 오도록
n = int(input())
t = list(map(int, input().split()))
sum, front = 0, 0
t.sort()
for i in t:
    sum += front
    sum += i
    front += i
print(sum)

# 앞에 사람이 걸린 시간 + 자신이 걸리는 시간
# 1 + (1+2) + (1+2+3) + (1+2+3+3) + (1+2+3+3+4)
# 1 + 3 + 6 + 9 + 13
