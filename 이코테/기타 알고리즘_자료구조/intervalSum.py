# 데이터의 개수 N과 데이터 입력받기
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 배열 계산
sumValue = 0
prefixSum = [0]
for i in data:
    sumValue += i
    prefixSum.append(sumValue)

# 구간 합 계산(세 번째 수부터 네번째 수까지)
left = 3
right = 4
print(prefixSum)
print(prefixSum[right] - prefixSum[left - 1])