# 문제 해결 아이디어

# 금광의 모든 위치에 대해 다음 세 가지만 고려
# 1. 왼쪽 위에서 오는 경우
# 2. 왼쪽 아래에서 오는 경우
# 3. 왼쩍에서 오는 경우
# 세 가지 경우 중에서 -> 가장 많은 금을 가지고 있는 경우를 테이블에 갱신

# 특정 위치에 대한 Optimal Soltion 값을 구하기 위해
# 왼쪽의 세 가지 위치에 대한 Optimal Solution을 구한 다음 -> 가장 많은 금을 가지고 있는 경우를 골라 
# 그곳에 + 현재 위치에서의 금의 값을 더해 -> 현재 위치까지 얻을 수 있는 금의 최댓값을 구할 수 있음.

# arr[i][j] = i행 j열에 존재하는 금의 양
# dp[i][j] = i행 j열까지의 최적의 해(얻을 수 있는 금의 최댓값)

# 점화식
# dp[i][j] = arr[j][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
# 이때, 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지? 체크
# 초기 데이터를 담는 변수 arr를 사용하지 않아도 O -> 바로 DP 테이블에 초기 데이터를 담아 DP 적용 가능

for i in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    # DP를 위한 2차원 DP 테이블 초기화
    dp = []
    idx = 0
    for _ in range(n):
         # 금광 정보를 입력받을 때 한 줄로 -> 열의 크기(m) 단위로 데이터를 slicing해서 dp 테이블에 담기
        dp.append(arr[idx:idx+m])  
        idx += m
        
    # DP 진행
    for j in range(1, m):   # 1 열부터 ~ m-1 열까지 (이전 위치에 대해) -> 각 열마다 전체 행을 확인
        for i in range(n):   # 0 행부터 ~ n-1 행까지
            # 왼쪽 위에서 오는 경우
            # 인덱스를 벗어난다면, 해당 경우의 값 = 0으로 초기화
            if i == 0: 
                left_up = 0   # 현재 위치의 행 인덱스가 0이라면, 그 위치로는, 이전 위치에서(위->아래로) 올 수 X
            else: 
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1: 
                left_down = 0   # 현재 위치의 행 인덱스가 n-1이라면, 그 위치로는, 이전 위치에서(아래->위로) 올 수 X
            else: 
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]

            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
            
    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][m-1])
    print(ans)