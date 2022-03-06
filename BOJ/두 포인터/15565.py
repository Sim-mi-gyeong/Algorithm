# 귀여운 라이언

n, k = map(int, input().split())
lst = list(map(int, input().split()))
cntRion = 0
end = 0
cnt = 0
ans = n 

for start in range(n):

    while cntRion < k and end < n:
        cnt += 1 

        if lst[end] == 1:
            cntRion += 1 
        if n == 1 and cntRion == 1:
            print(cnt)
            exit(0)

        end += 1 

    if cntRion >= k:
        start_ans = start
        ans = min(ans, cnt)

    if lst[start] == 1:
        cntRion -= 1 

    cnt -= 1

if ans == n: print(-1)   # 조건(cntRion 개수)을 만족하지 않아 ans 값이 변하지 않은 상태
else: print(ans)