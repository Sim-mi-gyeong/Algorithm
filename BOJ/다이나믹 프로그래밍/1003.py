# 피보나치 함수

# t = int(input())
# cnt0, cnt1 = 0, 0

# 재귀함수로 -> 시간초과
# def fibo(n):
#     global cnt0, cnt1
#     if n == 0:
#         cnt0 += 1
#         return 0
#     elif n == 1:
#         cnt1 += 1
#         return 1
#     else: return fibo(n-1) + fibo(n-2)

# for i in range(t):
#     n = int(input())
#     cnt0, cnt1 = 0, 0
#     fibo(n)
#     print(cnt0, cnt1)

# DP로 

for _ in range(int(input())):
    t = int(input())
    dp0, dp1= [0] * (t+1), [0] * (t+1)
    if t == 0:
        dp0[0], dp1[0] = 1, 0
    elif t ==1 :
        dp0[0], dp1[0] = 1, 0
        dp0[1], dp1[1] = 0, 1
    else:
        dp0[0], dp1[0] = 1, 0
        dp0[1], dp1[1] = 0, 1
        for i in range(2, t+1):
            dp0[i] = dp0[i-1] + dp0[i-2]
            dp1[i] = dp1[i-1] + dp1[i-2]
    print(dp0[t], dp1[t])
