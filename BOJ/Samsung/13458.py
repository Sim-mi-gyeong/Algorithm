# 시험 감독

n = int(input())
student = list(map(int, input().split()))
b, c = map(int, input().split())  # 총감독, 부감독 담당 수
cntB, cntC = 0, 0

for i in student:
    if i <= b:
        cntB += 1
    else:
        cntB += 1
        i -= b
        if i % c == 0:
            cntC += i // c
        else:
            cntC += i // c + 1

totalCnt = cntB + cntC
print(totalCnt)
