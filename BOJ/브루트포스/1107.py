# 리모컨

n = int(input())
m = int(input())
now = 100
if m == 0:
    ans = min(len(str(n)), abs(n - now))
    print(ans)
    exit(0)
else:
    lst = list(map(int, input().split()))
if n == now:
    print(0)
    exit(0)

cnt1 = abs(n - now)
cnt2, tmpCnt = 500000, 500000
for i in range(1000000 + 1):
    breakCheck = 0
    s = str(i)
    for j in s:
        if int(j) in lst:
            breakCheck = 1
            continue
    if breakCheck != 1:  # 고장난 숫자가 없으면, 이 숫자와 target 간 + / - 로 이동할 때 횟수 저장
        tmpNum = i
        cnt2 = abs(n - tmpNum) + len(s)
    tmpCnt = min(tmpCnt, cnt2)

ans = min(cnt1, tmpCnt)
print(ans)

# 가능한 버튼으로 target 채널과 가장 가까운 채널 찾는 방법 ? => Brute Force
# Brute Froce = Case 분류
# 1) 현재 채널에서 + / - 버튼으로만 이동
# 2) 모든 채널 순회 + 해당 채널에서 희망 채널까지 + / - 버튼으로 이동
