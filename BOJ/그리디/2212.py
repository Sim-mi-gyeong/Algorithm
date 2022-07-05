# 센서
# 각 집중국의 수신 가능영역의 거리의 합의 최솟값

n = int(input())
k = int(input())  # 최대 k 개 집중국 설치 가능 -> n 개의 센서가 하나의 집중국과 통신 가능
lst = list(map(int, input().split()))
lst.sort()

print(lst)

# 각 집중국은, 센서의 수신 가능 영역 조절 가능
# - 수신 가능 영역 = 고속도로 상에서 연결된 구간으로 나타남
# - N 개의 센서가 적어도 하나의 집중국과는 통신 가능해야 함
# - 집중국 유지비 문제 > 각 집중국의 수신 가능 영역 길이 합 최소

minVal = 1e9
start, end = lst[0], lst[-1]
check = [0] * (end + 1)


def dfs(cnt):
    global minVal

    if cnt <= k:
        # minVal = min(minVal, dist)
        return

    start, end = lst[0], lst[-1]
    for i in range(start, end + 1):
        # 하나 선택
        if not check[i]:
            check[i] = 1
            for j in lst:
                pass
        dfs(cnt + 1)
        check[i] = 0
        pass

    return minVal
