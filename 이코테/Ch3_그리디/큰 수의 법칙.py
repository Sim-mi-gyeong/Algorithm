n, m, k = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort(reverse=True)

cnt = 0   # 연산(더하기) 횟구
sum = 0

while(cnt != m):
    sum += arr[0] * k
    cnt += k
    sum += arr[1]
    cnt += 1
    
print(sum)

