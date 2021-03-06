# 문제 해결 아이디어
 
# 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS)로 알려진 전형적인 DP 문제 아이디어와 동일
# Ex) 하나의 수열 arr = {4, 3, 5, 8, 4, 11, 15}
# -> 가장 긴 증가하는 부분 수열 : {4, 5, 8, 11, 15}
# 본 문제는, [가장 긴 감소하는 부분 수열을 찾는 문제]로 치환 가능
# -> LIS 알고리즘을 조금 수정하여 적용 가능

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 확인
# D[i] = arr[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 점화식 : 모든 0 <= j < i에 대해, D[i] = max(D[i], d[J] + 1) if arr[j] < arr[i]

# i 는 각각의 원소
# 각 원소의 앞에 있는 다른 원소의 정보 확인(i 보다 앞쪽에 있는 원소 확인)
# 그 원소가, 현재 확인하고 있는 원소보다 작다면(즉, 앞쪽에 있는 원소가 뒤쪽의 원소(현재 확인하는 원소) 보다 작다면)
# 점화식에 따라 테이블 갱신

# 0 <= j < i : 모든 원소를 하나씩 확인하면서, 그 원소를 마지막으로 가지는 부분 수열의 최대 길이를 구하기 위헤
# 앞에 있는 원소들을 매번 확인해야 하므로 -> 전체 시간 복잡도는, 최악의 경우에 O(N^2)

# 모든 원소를 하나씩 확인하면서, 그 원소를 마지막 원소로 가지는 부분 수열

# 병사 배치하기
# 가장 먼저, 입력 받은 병사 정보의 순서를 뒤집기
# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행

n = int(input())
arr = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
arr.reverse()

# DP를 위한 1차원 DP 테이블 초기화
# 부분 수열을 만들 때, 각각의 원소 하나만 가지고 수열을 만들어도 길이는 1
# 각 원소를 마지막 원소로 가질 때 부분 수열의 길이 = 1 로 DP 테이블 초기화
dp = [1] * n

for i in range(1, n):   # 2번째 ~ 마지막 원소까지, 각 원소를 확인하며 -> 해당 원소를 마지막 원소로 설정
    for j in range(0, i):   # 증가하는 부분 수열의 최대 길이를 구할 수 있도록 -> 앞에 있는 모든 원소 중에서, 자기보다 해당 원소가 더 작은 경우에만 한해, 
        if arr[j] < arr[i]:
            # 현재 확인하고 있는 원소보다 더 작은 원소, 'j를 마지막 원소로' 가지는 부분 수열의 길이를 D[j]
            # -> 길이가 하나 더 늘어난 것이므로 D[j] + 1 Vs D[i]: 현재까지의 값
            dp[i] = max(dp[i], dp[j] + 1)   
            
# 열외해야 하는 병사의 최수 수 출력
print(n - max(dp))