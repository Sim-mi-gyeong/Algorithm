# 리모컨
#
now = 100
n = int(input())
m = int(input())  # 고장 버튼 수
if m >= 1:
    lst = list(map(int, input().split()))  # 고장난 버튼 종류
else:
    lst = []

a = []
for i in range(1, 10):
    if i not in lst:
        a.append(i)

if now == n:
    print(0)
    exit(0)

cnt0, cnt1, cnt2 = 0, 0, 0

tmpMax = 0
tmpMin = 0
tmp = ""
for i in a:
    tmp += str(i)
    tmpMin = min(tmpMin, int(tmp))

while True:
    for i in a:
        tmp += str(i)
        tmpMin = min(tmpMin, int(tmp))

    if abs(tmpMin - n) < abs(tmpMax - n):
        cnt1 += tmpMin - n
    else:
        cnt2 += tmpMax - n


cnt0 = n - now


# tmp = ""
# for i in str(n):
#     if int(i) not in lst:
#         tmp += i
#         cnt += 1
#     print("tmp : ", tmp, "일 때 cnt : ", cnt)

# if cnt != len(str(n)):
#     pass

# print(cnt)
